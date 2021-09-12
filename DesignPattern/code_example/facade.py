class InvoiceChecker:
    def check(self):
        print("InvoiceChecker check")


class PackageChecker:

    def check(self):
        print("PackageChecker check")


class Something:

    def anything(self):
        print("Something anything")


class OutboundFacade:

    def __init__(self):
        self._invoice_checker = InvoiceChecker()
        self._package_checker = PackageChecker()
        self._something = Something()

    def operate(self):
        self._invoice_checker.check()
        self._package_checker.check()
        self._something.anything()


def client_code():
    facade = OutboundFacade()
    facade.operate()

"""
InvoiceChecker check
PackageChecker check
Something anything
"""

client_code()
