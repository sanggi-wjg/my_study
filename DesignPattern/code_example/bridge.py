from abc import ABC, abstractmethod


class RequestTrackingInterface(ABC):

    @abstractmethod
    def request(self) -> str:
        pass

    @abstractmethod
    def parse_response(self, response: str) -> str:
        pass


class RequestTrackingTypeA(RequestTrackingInterface):

    def request(self) -> str:
        return 'A response'

    def parse_response(self, response: str) -> str:
        return response


class RequestTrackingTypeB(RequestTrackingInterface):

    def request(self) -> str:
        return 'B response'

    def parse_response(self, response: str) -> str:
        return response


class RequestTracking(object):

    def __init__(self, tracking_interface: RequestTrackingInterface):
        self._tracking_interface = tracking_interface

    @property
    def tracking_interface(self):
        return self._tracking_interface

    def operate(self):
        response = self.tracking_interface.request()
        return self.tracking_interface.parse_response(response)


class RequestTrackingEMS(RequestTracking):

    def operate(self):
        print('EMS는 앞에서 뭔 작업을 해줘야 합니다.')
        return super(RequestTrackingEMS, self).operate()


"""
A response

EMS는 앞에서 뭔 작업을 해줘야 합니다.
B response
"""


def client_code():
    tracking = RequestTracking(RequestTrackingTypeA())
    result = tracking.operate()
    print(result)

    tracking_ems = RequestTrackingEMS(RequestTrackingTypeB())
    result = tracking_ems.operate()
    print(result)


client_code()
