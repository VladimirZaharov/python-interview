class ItemDiscount:
    __product = "phone"
    __price = 12000

class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        print(f'{self._ItemDiscount__product} - {self._ItemDiscount__price}')

a = ItemDiscount()
b = ItemDiscountReport()
b.get_parent_data()