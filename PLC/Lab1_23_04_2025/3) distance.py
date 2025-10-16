x1=float(input("Enter x coordinate of 1st point: "))
y1=float(input("Enter y coordinate of 1st point: "))
x2=float(input("Enter x coordinate of 2nd point: "))
y2=float(input("Enter y coordinate of 2nd point: "))

distance = (((x2-x1)**2)+((y2-y1)**2))**0.5

print(f"The distance between point ({x1},{y1}) and ({x2},{y2}) is: {distance}")
