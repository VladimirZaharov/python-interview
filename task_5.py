class ItemDiscount:
    product = "phone"
    price = 12000

class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        print(f'{self.product} - {self.price}')

class ItemDiscountReportChild(ItemDiscount):
    def __init__(self, discount):
        self.discount = discount
    def __str__(self):
        return f'{self.price - self.price/100*self.discount}'

a = ItemDiscountReportChild(5)
print(a)