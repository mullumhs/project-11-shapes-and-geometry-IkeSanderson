from shapes import Shape, Rectangle, Circle
from utility import get_int

def menu():
    print("R for Rectangle")
    print("C for Circle")
    choice = input("Please Select which shape you would like to Create:")
    if choice.upper() == "R":
        length = get_int(input("Please Enter the Length of your Rectangle:"))
        width = get_int(input("Please Enter the Width of your Rectangle:"))
        
        rect = Rectangle(length, width)
        print(f"Area: {rect.calculate_area()}")
        print(f"Perimeter: {rect.calculate_perimeter()}")
    if choice.upper() == "C":
        radius =int(input("Please Enter the Radius of your Circle:"))
        circ = Circle(radius)
        print(f"Area: {circ.calculate_area()}")
        print(f"Perimeter: {circ.calculate_perimeter()}")




while True:
    menu()
    print()
