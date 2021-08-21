import functools
from typing import Callable


def catch_error(catch: tuple):
    def decorator(func: Callable):

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except catch as e:
                print(e)

        return wrapper

    return decorator


class DeviceControllerError(Exception):
    pass


class DeviceShutdownError(DeviceControllerError):
    pass


class DeviceController:

    @catch_error(catch = (DeviceControllerError, DeviceShutdownError))
    def shutdown(self):
        device = self.get_handle()
        device.pause()
        device.clear_queue()
        device.close()

    def get_handle(self, device_id: int):
        ...
        raise DeviceControllerError('Invalid device handle')


service = DeviceController()
service.shutdown()
