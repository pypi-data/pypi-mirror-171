import asyncio
import inspect
import uuid
from typing import Optional, Type

from django.http import HttpResponse, HttpRequest

from .collector import (
    DjangoDataCollectorBase,
    DjangoDataTopCollector,
    DjangoDataBottomCollector,
)


class _MiddlewareBase:
    sync_capable = True
    async_capable = True

    def __init__(self, get_response):
        self.get_response = get_response
        self._async_check()

    def _async_check(self):
        """
        If get_response is a coroutine function, turns us into async mode so
        a thread is not consumed during a whole request.
        """
        if asyncio.iscoroutinefunction(self.get_response):
            # Mark the class as async-capable, but do the actual switch
            # inside __call__ to avoid swapping out dunder methods
            self._is_coroutine = getattr(asyncio.coroutines, "_is_coroutine")


class DjangoDataTopMiddleware(_MiddlewareBase):
    """put this middleware at the top of middleware stack"""

    COLLECTOR_CLASS: Type[DjangoDataTopCollector] = DjangoDataTopCollector

    def __init__(self, get_response):
        super(DjangoDataTopMiddleware, self).__init__(get_response)
        self.data_collector: Optional[DjangoDataCollectorBase] = None

    def __call__(self, request: HttpRequest):
        # attach a request_id for to this request
        # it maybe used to connect user behavior with the db data
        request.request_id = uuid.uuid4().hex

        if asyncio.iscoroutinefunction(self.get_response):
            return self.__acall__(request)

        self.data_collector = self.COLLECTOR_CLASS()
        self.data_collector.attach_request(request)
        response: HttpResponse = self.get_response(request)

        self.data_collector.attach_response(response)
        self.data_collector.do_collect()
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        """extract view object and save refer to it in request, so we can access it after response generated"""
        if inspect.ismethod(view_func):
            setattr(request, "view_func_self", view_func.__self__)

    async def __acall__(self, request):
        self.data_collector = self.COLLECTOR_CLASS()
        self.data_collector.attach_request(request)
        response = await self.get_response(request)
        self.data_collector.attach_response(response)
        # DB related operation is async-unsafe
        f = asyncio.get_running_loop().run_in_executor(
            None, self.data_collector.do_collect
        )
        await f
        return response


class DjangoDataBottomMiddleware(DjangoDataTopMiddleware):
    """put this middleware at the bottom of middleware stack"""

    COLLECTOR_CLASS: Type[DjangoDataBottomCollector] = DjangoDataBottomCollector
