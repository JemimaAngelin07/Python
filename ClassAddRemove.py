class ShoppingCart:
    def __init__(self):
        self.items=[]

    def add_items(self,item_name,qty):
        item=(item_name,qty)
        self.items.append(item)

    def remove_item(self,item_name):
        for item in self.items:
            if item[0] == item_name:
                self.items.remove(item)
                break

    def cal_item(self):
        total=0
        for item in self.items:
            total +=item[1]
        return total
                       
cart=ShoppingCart()
cart.add_items("Mango",200)
cart.add_items("Orange",100)
cart.add_items("Kiwi",300)
cart.add_items("Apple",100)

print("Items in Cart:")
for item in cart.items:
    print(item[0],"-",item[1])

total_qty=cart.cal_item()
print("Total:",total_qty)

cart.remove_item("Apple")
print("\nAfter Removing From Cart:")
for item in cart.items:
    print(item[0],"-",item[1])

total_qty=cart.cal_item()
print("Total:",total_qty)    