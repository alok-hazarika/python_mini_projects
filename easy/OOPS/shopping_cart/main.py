# Write a Python program to create a class representing a shopping cart. 
# Include methods for adding and removing items, and calculating the total price.

class ShoppingCart:
    def __init__(self, item_name=[], qty=[], price=[]) :
        self.item_name = item_name
        self.qty = qty
        self.price = price
        self.total = 0
    
    def add_items(self, item_name, qty, price):
        counter = False
        for i in range(len(self.item_name)):
            if self.item_name[i] == item_name:
                counter = True
        if counter == True:
            item_idx = self.item_name.index(item_name)
            self.qty[item_idx] = self.qty[item_idx] + qty
            self.price[item_idx] = self.price[item_idx] + (qty * price)
        else:  
            self.item_name.append(item_name)
            self.qty.append(qty)
            self.price.append(price * qty)

    def remove_items(self, item_name, qty, price):
        item_idx = self.item_name.index(item_name)
        if self.qty[item_idx] == qty:
            self.price.pop(item_idx)
            self.item_name.pop(item_idx)
            self.qty.pop(item_idx)
        else:
            self.qty[item_idx] = self.qty[item_idx] - qty
            self.price[item_idx] = self.price[item_idx] - (qty * price)

    def calculate_total(self):
        for i in range(len(self.item_name)):
            self.total += self.price[i]
        return self.total
    
    def view_cart(self):
        return self.item_name, self.qty, self.price
    
        
    

my_cart = ShoppingCart()
my_cart.add_items("Mango", 2, 140)
my_cart.add_items("Apple", 1, 120)
my_cart.add_items("Kiwi", 4, 160)
my_cart.remove_items("Kiwi", 2, 160)
my_cart.add_items("Orange", 1, 120)
my_cart.add_items("Apple", 2, 100)

print(my_cart.calculate_total())
print(my_cart.view_cart())
