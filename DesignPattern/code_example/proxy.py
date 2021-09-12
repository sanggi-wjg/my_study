from abc import ABC, abstractmethod


class RequestAbs(ABC):

    @abstractmethod
    def request(self):
        pass


class Request(RequestAbs):

    def request(self):
        print('Request : request')


class ProxyRequest(RequestAbs):

    def __init__(self, request: RequestAbs):
        self._request = request

    def request(self):
        if self.check_access():
            self._request.request()

    def check_access(self) -> bool:
        print('check access')
        return True


def client_code():
    request = Request()
    request.request()

    proxy_request = ProxyRequest(request)
    proxy_request.request()


"""
Request : request

check access
Request : request
"""
client_code()
