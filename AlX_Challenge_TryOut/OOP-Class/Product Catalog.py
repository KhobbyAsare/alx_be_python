class ProductCatalog:
    def __init__(self, name, price:float, quantity:int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def totalProductValue(self):
        total = self.price * self.quantity
        return  f"{self.name} cost {total}"


# Polymorphism: hidden the complex implementation and give the user a way to display the total of the product
def displayTotals(productObject):
    print(productObject.totalProductValue())


products = [
    ProductCatalog("laptop", 2000.0,5 ),
    ProductCatalog("Car", 600000.0,2 )
]


for product in products:
    displayTotals(product)
