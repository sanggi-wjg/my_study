from abc import ABC, abstractmethod
from typing import Any


class ServiceCheckResult(object):

    def __init__(self):
        self._service_healths = []

    def add(self, health_result):
        self._service_healths.append(health_result)

    def show_healths(self):
        print('\n'.join(self._service_healths))


class ServiceCheckBuilder(ABC):

    @property
    @abstractmethod
    def result(self):
        pass

    @abstractmethod
    def check_important(self):
        pass

    @abstractmethod
    def check_all(self):
        pass


class ServiceHealthCheckBuilder(ServiceCheckBuilder):

    def __init__(self):
        self._result = ServiceCheckResult()

    @property
    def result(self) -> ServiceCheckResult:
        return self._result

    def check_important(self):
        print('Check /auth')
        print('Check /user')

    def check_all(self):
        print('Check /auth')
        print('Check /user')
        print('Check /something')
        print('Check /anything')


class ServiceStatusCheckerBuilder(ServiceCheckBuilder):

    def __init__(self):
        self._result = ServiceCheckResult()

    @property
    def result(self) -> ServiceCheckResult:
        return self._result

    def check_important(self):
        print('Check MySQL')

    def check_all(self):
        print('Check MySQL')
        print('Check Redis')
        print('Check Celery')


class ServiceCheckDirector(object):

    def __init__(self):
        self._builder = None

    @property
    def builder(self) -> ServiceCheckBuilder:
        return self._builder

    @builder.setter
    def builder(self, builder: ServiceCheckBuilder):
        self._builder = builder

    def check_only_important_service(self):
        print('\n[Check only important services]')
        self.builder.check_important()

    def check_all_service(self):
        print('\n[Check all services]')
        self.builder.check_all()


def client_code():
    director = ServiceCheckDirector()
    health_builder = ServiceHealthCheckBuilder()

    director.builder = health_builder
    director.check_only_important_service()
    director.check_all_service()

    director.builder = ServiceStatusCheckerBuilder()
    director.check_only_important_service()
    director.check_all_service()


"""
[Check only important services]
Check /auth
Check /user

[Check all services]
Check /auth
Check /user
Check /something
Check /anything

[Check only important services]
Check MySQL

[Check all services]
Check MySQL
Check Redis
Check Celery
"""
client_code()
