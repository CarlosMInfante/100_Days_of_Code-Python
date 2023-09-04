import math


def paint_calc(height, width, cover):
    area = height * width
    # Rounding up because you have to buy whole cans of paint.
    number_of_cans = math.ceil(area / cover)
    print(f"You'll need {number_of_cans} cans of paint.")


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
