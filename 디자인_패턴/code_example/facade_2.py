from abc import ABC, abstractmethod


class CheckerInterface(ABC):

    @abstractmethod
    def check(self):
        pass


class InvoiceCheckerInterface(CheckerInterface):

    @abstractmethod
    def is_valid(self):
        pass

    @abstractmethod
    def is_something(self):
        pass

    def check(self):
        self.is_valid()
        self.is_something()


class EMSInvoiceChecker(InvoiceCheckerInterface):

    def is_valid(self):
        print('EMSInvoiceChecker is_valid')

    def is_something(self):
        print('EMSInvoiceChecker is_something')


class DaehanInvoiceChecker(InvoiceCheckerInterface):

    def is_valid(self):
        print('DaehanInvoiceChecker is_valid')

    def is_something(self):
        print('DaehanInvoiceChecker is_something')


class PackageChecker(CheckerInterface):

    def check(self):
        print("PackageChecker check")


class OutboundFacade:

    def __init__(self, transfer_company_name: str):
        # 이것도 많아지면 팩토리로 바꿔서 구현
        if transfer_company_name == 'EMS':
            self._invoice_checker = EMSInvoiceChecker()
        elif transfer_company_name == 'DAEHAN':
            self._invoice_checker = DaehanInvoiceChecker()
        self._package_checker = PackageChecker()

    def operate(self):
        self._invoice_checker.check()
        self._package_checker.check()


def client_code():
    facade = OutboundFacade('EMS')
    facade.operate()

    facade = OutboundFacade('DAEHAN')
    facade.operate()

"""
EMSInvoiceChecker is_valid
EMSInvoiceChecker is_something
PackageChecker check

DaehanInvoiceChecker is_valid
DaehanInvoiceChecker is_something
PackageChecker check
"""
client_code()
