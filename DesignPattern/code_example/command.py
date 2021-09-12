from abc import ABC, abstractmethod


class DeviceCommand(ABC):

    @abstractmethod
    def operate(self):
        pass


class Heater(object):

    def power_on(self):
        print('Heater power_on')


class Lamp(object):

    def power_on(self):
        print('Lamp power_on')


class HeaterOnCommand(DeviceCommand):

    def __init__(self, heater: Heater):
        self._heater = heater

    @property
    def heater(self):
        return self._heater

    def operate(self):
        self.heater.power_on()


class LampOnCommand(DeviceCommand):

    def __init__(self, lamp: Lamp):
        self._lamp = lamp

    @property
    def lamp(self):
        return self._lamp

    def operate(self):
        self.lamp.power_on()


class RemoteController:
    """
    첫번째 스타일
    """

    def __init__(self):
        self._device_command = None

    def set_command(self, device_command: DeviceCommand):
        self._device_command = device_command

    @property
    def device_command(self):
        return self._device_command

    def click_button(self):
        self.device_command.operate()


class Invoker:
    """
    두번째 스타일
    """

    def __init__(self):
        self._on_start = None
        self._on_finish = None

    def set_command_on_start(self, device_command: DeviceCommand):
        self._on_start = device_command

    def set_command_on_finish(self, device_command: DeviceCommand):
        self._on_finish = device_command

    @property
    def on_start(self):
        return self._on_start

    @property
    def on_finish(self):
        return self._on_finish

    def run(self):
        self.on_start.operate()
        self.on_finish.operate()


def client_code():
    heater_command = HeaterOnCommand(Heater())
    lamp_command = LampOnCommand(Lamp())
    
    # 첫번째 스타일
    remotecon = RemoteController()
    remotecon.set_command(heater_command)
    remotecon.click_button()

    remotecon.set_command(lamp_command)
    remotecon.click_button()

    # 두번째 스타일
    invoker = Invoker()
    invoker.set_command_on_start(heater_command)
    invoker.set_command_on_finish(lamp_command)
    invoker.run()


"""
Heater power_on
Lamp power_on

Heater power_on
Lamp power_on
"""

client_code()
