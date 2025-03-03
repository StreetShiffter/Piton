def circle_area(r: int) -> float:
    PI = 3.14
    circleArea = PI * r**2
    return circleArea


def format_description(r, area):
    return "Radius is " + str(r) + "; area is " + str(round(area, 2))


def get_info(r: int):
    area = circle_area(r)
    description = format_description(r, area)
    print(description)


radius = int(input("Enter circle radius (int): "))
get_info(radius)
