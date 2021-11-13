class ItemDiscount:
    __product = "phone"
    __price = 12000

class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        print(f'{self.__product} - {self.__price}')

a = ItemDiscount()
b = ItemDiscountReport()
b.get_parent_data()