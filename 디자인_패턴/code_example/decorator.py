from abc import ABC, abstractmethod


class PickingList(ABC):

    def get_data(self):
        print('PickingList get_data')

    def make_list(self):
        print('PickingList make_list')

    @abstractmethod
    def render(self):
        pass


class HTMLRender(PickingList):

    def render(self):
        print('HTMLRender render')
        self.get_data()
        self.make_list()


class PickingListRenderDecorator(PickingList):

    def __init__(self, picking_list: PickingList):
        self._picking_list = picking_list

    @property
    def picking_list(self):
        return self._picking_list

    def render(self):
        self.picking_list.render()


class BarcodeRenderDecorator(PickingListRenderDecorator):

    def add_barcode(self):
        print('BarcodeRenderDecorator add_barcode')

    def render(self):
        super(BarcodeRenderDecorator, self).render()
        self.add_barcode()


class RackCodeRenderDecorator(PickingListRenderDecorator):

    def add_rack_code(self):
        print('RackCodeRenderDecorator add_rack_code')

    def render(self):
        super(RackCodeRenderDecorator, self).render()
        self.add_rack_code()


def client_code():
    picking_list = RackCodeRenderDecorator(HTMLRender())
    picking_list.render()

    picking_list = RackCodeRenderDecorator(BarcodeRenderDecorator(HTMLRender()))
    picking_list.render()


"""
HTMLRender render
PickingList get_data
PickingList make_list
RackCodeRenderDecorator add_rack_code

HTMLRender render
PickingList get_data
PickingList make_list
BarcodeRenderDecorator add_barcode
RackCodeRenderDecorator add_rack_code
"""

client_code()
