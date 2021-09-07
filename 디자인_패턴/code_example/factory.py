from abc import ABC, abstractmethod


class PrintOutput(ABC):

    @abstractmethod
    def get_output(self) -> str:
        pass


class YTOOutput(PrintOutput):

    def get_output(self) -> str:
        return 'YTO output'


class EMSOutput(PrintOutput):

    def get_output(self) -> str:
        return 'EMS output'


class PrintOutputFactory(object):

    def create(self, print_type: str) -> PrintOutput:
        if print_type == 'YTO':
            return YTOOutput()
        elif print_type == 'EMS':
            return EMSOutput()
        else:
            raise Exception('invalid print_type')


def client_code():
    factory = PrintOutputFactory()
    print_output = factory.create('YTO')
    output = print_output.get_output()
    print(output)
