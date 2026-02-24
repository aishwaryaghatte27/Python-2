from shapes import circle_area, rectangle_area, triangle_area

print("=== Shape Area Calculator ===")
print("1. Circle")
print("2. Rectangle")
print("3. Triangle")
choice = input("Enter your choice (1/2/3): ")

if choice == '1':
    r = float(input("Enter radius: "))
    area = circle_area(r)
    print(f"Area of circle = {area:.2f}")

elif choice == '2':
    l = float(input("Enter length: "))
    w = float(input("Enter width: "))
    area = rectangle_area(l, w)
    print(f"Area of rectangle = {area:.2f}")

elif choice == '3':
    b = float(input("Enter base: "))
    h = float(input("Enter height: "))
    area = triangle_area(b, h)
    print(f"Area of triangle = {area:.2f}")

else:
    print("Invalid choice!")
