from shapes import Shape, Rectangle, Circle
from utility import get_int, print_debug 
debug = True
def menu():
    print("R for Rectangle")
    print("C for Circle")
    choice = input("Please Select which shape you would like to Create:")
    
    if choice.upper() == "R":
        print_debug(debug, "Chose Rectangle")
        length = get_int("Please Enter the Length of your Rectangle:")
        width = get_int("Please Enter the Width of your Rectangle:")
        
        rect = Rectangle(length, width)
        print_debug(debug, f"{length} x {width}")
        print(f"Area: {rect.calculate_area()}")

        print_debug(debug, f"2({length} + {width})")
        print(f"Perimeter: {rect.calculate_perimeter()}")

    if choice.upper() == "C":
        print_debug(debug, "Chose Circle")
        radius = get_int("Please Enter the Radius of your Circle:")
        circ = Circle(radius)

        print_debug(debug, f"Pi x {radius} Squared")
        print(f"Area: {circ.calculate_area()}")

        print_debug(debug, f" 2 x Pi x {radius}")
        print(f"Circumference: {circ.calculate_perimeter()}")




while True:
    menu()
    print()
