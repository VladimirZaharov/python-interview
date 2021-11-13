class ItemDiscount:
    product = "phone"
    price = 12000

# class ItemDiscountReport(ItemDiscount):
#     def get_parent_data(self):
#         print(f'{self.product} - {self.price}')

class ItemDiscountReportProduct(ItemDiscount):
    def get_info(self):
        return f'название продукта - {self.product}'

class ItemDiscountReportPrice(ItemDiscount):
    def get_info(self):
        return f'Цена - {self.price}'

# 1.
a = ItemDiscountReportPrice()
b = ItemDiscountReportProduct()
print(a.get_info())
print(b.get_info())
# # 2.
print(ItemDiscountReportProduct.get_info(ItemDiscount))
print(ItemDiscountReportPrice.get_info(ItemDiscount))
# 3.
print(ItemDiscountReportProduct.__dict__['get_info'](ItemDiscount))
print(ItemDiscountReportPrice.__dict__['get_info'](ItemDiscount))
