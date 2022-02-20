# Program to calculate the number of cans required to paint a wall

wall_h = int(input("Height of wall: "))
wall_w = int(input("Width of wall: "))
coverage_per_can = 5

number_of_cans = 0

def paint_calc(height, width, cover):
    number_of_cans = round((height*width) / cover)
    print(f"You will need {number_of_cans} cans of paint.")

paint_calc(height=wall_h, width=wall_w, cover=coverage_per_can)

