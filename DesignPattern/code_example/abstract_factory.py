from abc import ABC, abstractmethod


class Keyboard(ABC):

    @abstractmethod
    def type(self) -> str:
        pass


class LogitechKeyboard(Keyboard):

    def type(self) -> str:
        return 'Logitech typed'


class MSKeyboard(Keyboard):

    def type(self) -> str:
        return 'MS typed'


class Mouse(ABC):

    @abstractmethod
    def click(self) -> str:
        pass


class LogitechMouse(Mouse):

    def click(self) -> str:
        return 'Logitech clicked'


class MSMouse(Mouse):

    def click(self) -> str:
        return 'MS clicked'


class ComputerModuleFactory(ABC):

    @abstractmethod
    def create_keyboard(self) -> Keyboard:
        pass

    @abstractmethod
    def create_mouse(self) -> Mouse:
        pass


class LogitechComputerModuleFactory(ComputerModuleFactory):

    def create_keyboard(self) -> Keyboard:
        return LogitechKeyboard()

    def create_mouse(self) -> Mouse:
        return LogitechMouse()


class MSComputerModuleFactory(ComputerModuleFactory):

    def create_keyboard(self) -> Keyboard:
        return MSKeyboard()

    def create_mouse(self) -> Mouse:
        return MSMouse()


def create(computer_module_name: str) -> ComputerModuleFactory:
    if computer_module_name == 'MS':
        return MSComputerModuleFactory()
    elif computer_module_name == 'Logitech':
        return LogitechComputerModuleFactory()
    else:
        raise Exception('invalid computer_module_name')


def client_code():
    factory = create('MS')
    keyboard = factory.create_keyboard()
    mouse = factory.create_mouse()

    print(keyboard.type())
    print(mouse.click())
