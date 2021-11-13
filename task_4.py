class ItemDiscount:
    product = "phone"
    price = 12000

class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        print(f'{self.product} - {self.price}')

a = ItemDiscount()
b = ItemDiscountReport()
b.get_parent_data()
ItemDiscount.price = 15000
a = ItemDiscount()
b = ItemDiscountReport()
b.get_parent_data()