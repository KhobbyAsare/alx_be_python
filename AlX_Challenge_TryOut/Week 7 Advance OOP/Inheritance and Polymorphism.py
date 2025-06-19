class Shape:
    def __init__(self, width, length, radius):
        self.radius = radius
        self.width = width
        self.length = length

    def calculate_area(self, shape_name:str):
        match shape_name:
            case "rectangle":
                return self.width * self.length
            case "square":
                return 3.14 * self.radius^2



class Rectangle(Shape):
    def __init__(self, width, length, radius):
        super().__init__(width, length, radius)




rectangle1 = Rectangle(2,5, 4)
print(rectangle1.calculate_area("rectangle"))

