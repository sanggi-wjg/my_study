from abc import ABC, abstractmethod
from typing import Any


class RequestOutboundInterface(ABC):

    @abstractmethod
    def set_request(self):
        pass

    @abstractmethod
    def handle_response(self):
        pass

    @abstractmethod
    def save(self):
        pass


class RequestOutboundA(RequestOutboundInterface):

    def set_request(self):
        print('A set_request')

    def handle_response(self):
        print('A handle_response')

    def save(self):
        print('A save')


class RequestOutboundRepeatPageInterface(ABC):

    @abstractmethod
    def set_request(self):
        pass

    @abstractmethod
    def handle_response(self):
        pass

    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def repeat_page(self):
        pass


class RequestOutboundRepeatPageAdapter(RequestOutboundInterface):

    def __init__(self, interface: RequestOutboundRepeatPageInterface):
        self._interface = interface

    @property
    def interface(self):
        return self._interface

    def set_request(self):
        self.interface.set_request()

    def handle_response(self):
        self.interface.handle_response()

    def save(self):
        self.interface.save()
        self.interface.repeat_page()


class RequestOutboundB(RequestOutboundRepeatPageInterface):

    def set_request(self):
        print('B set_request')

    def handle_response(self):
        print('B handle_response')

    def repeat_page(self):
        print('B repeat_page')

    def save(self):
        print('B save')


def create(partner) -> RequestOutboundInterface:
    if partner == 'A':
        return RequestOutboundA()
    elif partner == 'B':
        return RequestOutboundRepeatPageAdapter(RequestOutboundB())


def client_code():
    service_a = create('A')
    service_a.set_request()
    service_a.handle_response()
    service_a.save()

    service_b = create('B')
    service_b.set_request()
    service_b.handle_response()
    service_b.save()


"""
A set_request
A handle_response
A save

B set_request
B handle_response
B save
B repeat_page
"""
client_code()
