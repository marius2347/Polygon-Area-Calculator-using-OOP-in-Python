# Class Rectangle
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    # Set Width
    def set_width(self, width):
        self.width = width
    # Set Height
    def set_height(self, height):
        self.height = height
    # Get Area
    def get_area(self):
        return self.width * self.height
    # Get Perimeter
    def get_perimeter(self):
        return 2 * self.width + 2 * self.height
    # Get Picture
    def get_picture(self):
        if self.width >= 50 or self.height >= 50:
            return "Too big fore picture"
        string = ""
        for i in range(0, self.height):
            for j in range(0, self.width):
                string += "*"
            string += "\n"
        return str(string)
    # Get Diagonal
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5



# Class Square with SubClass Rectangle
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
    def set_side(self, side):
        self.width = side
        self.height = side



# Rectangle uses
rec = Rectangle(10, 3)
rec.set_width(int(input("Set width of the RECTANGLE: ")))
rec.set_height(int(input("Set height of the RECTANGLE: ")))
print("Area of the rectangle is: {} SQUARE METERS".format(rec.get_area()))
print("Perimeter of the rectangle is: {} METERS".format(rec.get_perimeter()))
print("Diagonal is: {} ".format(rec.get_diagonal()))
print("The picture is: ")
print(rec.get_picture())
print('\n')

# Square uses
sq = Square(9)
sq.set_side(int(input("Set side length of the SQUARE: ")))
print("Area of the square is: {} SQUARE METERS".format(sq.get_area()))
print("Perimeter of the rectangle is: {} METERS".format(sq.get_perimeter()))
print("Diagonal is: {} ".format(sq.get_diagonal()))
print("The picture is: ")
print(sq.get_picture())

