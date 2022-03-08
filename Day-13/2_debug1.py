# Reproduce the bug

# from random import randint
# dice_imgs = ["1", "2", "3", "4", "5", "6"]
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num])

# Above code will give error in line 6
# as the list index will go out of range


# Fixed code
from random import randint
dice_imgs = ["1", "2", "3", "4", "5", "6"]
dice_num = randint(0, 5)
print(dice_imgs[dice_num])



