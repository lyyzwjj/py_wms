from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse


# class BlockedIpsMiddleware(MiddlewareMixin):
#     '''中间件类'''
#     EXCLUDE_IPS = ['192.168.232.1']
#
#     def process_view(self, request, view_func, *view_arg, **view_kwargs):
#         '''调用视图函数之前调用此函数'''
#         user_ip = request.META['REMOTE_ADDR']
#         if user_ip in BlockedIpsMiddleware.EXCLUDE_IPS:
#             return HttpResponse('<h1>Forbidden</h1>')


class BlockedIpsMiddleware(MiddlewareMixin):
    '''中间件类'''
    EXCLUDE_IPS = ['192.168.232.1']

    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def process_request(self, request):
        print('中间件1的请求')

    def process_response(self, request, response):
        print('中间件1的返回')
        return response

    # def process_view(self, request, view_func, *view_arg, **view_kwargs):
    # '''调用视图函数之前调用此函数'''
    #         user_ip = request.META['REMOTE_ADDR']
    #         if user_ip in BlockedIpsMiddleware.EXCLUDE_IPS:
    #             return HttpResponse('<h1>Forbidden</h1>')

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        print('中间件1的 view前调用')
        '''调用视图函数之前调用此函数'''
        user_ip = request.META['REMOTE_ADDR']
        if user_ip in BlockedIpsMiddleware.EXCLUDE_IPS:
            return HttpResponse('<h1>Forbidden</h1>')
        response = self.get_response(request)
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        print('中间件1的 view之后调用')
        return response
