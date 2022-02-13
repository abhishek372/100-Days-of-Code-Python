# Program to mark a spot with an X

row1 = ["◻️", "◻️", "◻️"]
row2 = ["◻️", "◻️", "◻️"]
row3 = ["◻️", "◻️", "◻️"]

map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

position = int(position)

row = position % 10
column = position // 10

map[row-1][column-1] = 'X'

print(f"{row1}\n{row2}\n{row3}")

