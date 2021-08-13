class DeviceControllerError(Exception):
    pass


class DeviceShutdownError(DeviceControllerError):
    pass


class DeviceController:

    def shutdown(self):
        try:
            self.try_shutdown()
        except (DeviceControllerError, DeviceShutdownError) as e:
            ...
            logger.error()

    def try_shutdown(self):
        device = self.get_handle()
        device.pause()
        device.clear_queue()
        device.close()

    def get_handle(self, device_id: int):
        ...
        raise DeviceControllerError('Invalid device handle')
