from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse


class BlockedIpsMiddleware(MiddlewareMixin):
    '''中间件类'''
    EXCLUDE_IPS = ['192.168.232.1']

    def process_view(self, request, callback, callback_args, callback_kwargs):
        '''调用视图函数之前调用此函数'''
        user_ip = request.META['REMOTE_ADDR']
        if user_ip in BlockedIpsMiddleware.EXCLUDE_IPS:
            return HttpResponse('<h1>Forbidden</h1>')


# class BlockedIpsMiddleware(MiddlewareMixin):
#     '''中间件类'''
#     EXCLUDE_IPS = ['192.168.232.1']
#
#     def __init__(self, get_response):
#         self.get_response = get_response
#         # One-time configuration and initialization.
#
#     def __call__(self, request):
#         # Code to be executed for each request before
#         # the view (and later middleware) are called.
#         print('中间件1的 view前调用')
#         '''调用视图函数之前调用此函数'''
#         user_ip = request.META['REMOTE_ADDR']
#         if user_ip in BlockedIpsMiddleware.EXCLUDE_IPS:
#             return HttpResponse('<h1>Forbidden</h1>')
#         response = self.get_response(request)
#         # Code to be executed for each request before
#         # the view (and later middleware) are called.
#         print('中间件1的 view之后调用')
#         return response
class TestMiddleware(MiddlewareMixin):
    '''中间件类'''

    # def __init__(self):
    #     '''服务器重启之后，接受第一个请求时候调用'''
    #     print('----init----')

    def process_request(self, request):
        '''产生了request对象之后,url匹配之前调用'''
        print('----process_request----')
        # return HttpResponse('process_request')

    def process_view(self, request, callback, callback_args, callback_kwargs):
        '''url匹配之后,试图函数调用之前调用'''
        print('----process_view----')
        # return HttpResponse('process_view')

    def process_response(self, request, response):
        '''视图函数调用之后,内容返回到浏览器之'''
        print('----process_response----')
        return response

    def process_exception(self, request, exception):
        '''视图函数发生异常时候调用'''
        print('----process_response----')


# 异常中间调用顺序与注册顺序相反
class ExceptionTest1Middleware(MiddlewareMixin):
    def process_exception(self, request, exception):
        '''视图函数发生异常时候调用'''
        print(exception)
        print('----process_response1----')


class ExceptionTest2Middleware(MiddlewareMixin):
    def process_exception(self, request, exception):
        '''视图函数发生异常时候调用'''
        print('----process_response2----')
