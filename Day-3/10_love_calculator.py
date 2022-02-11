# Love Calculator program

# Greeting Message
print("Welcome to the Love Calculator")

# Inputs
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

# Lowercase of strings
name1_lowercase = name1.lower()
name2_lowercase = name2.lower()

# Counting the each letters of true and love from given names
t_count = name1_lowercase.count("t") + name2_lowercase.count("t")
r_count = name1_lowercase.count("r") + name2_lowercase.count("r")
u_count = name1_lowercase.count("u") + name2_lowercase.count("u")
e_count = name1_lowercase.count("e") + name2_lowercase.count("e")
l_count = name1_lowercase.count("l") + name2_lowercase.count("l")
o_count = name1_lowercase.count("o") + name2_lowercase.count("o")
v_count = name1_lowercase.count("v") + name2_lowercase.count("v")
e_count = name1_lowercase.count("e") + name2_lowercase.count("e")

# Sum of all letters of true and love
true_count = t_count + r_count + u_count + e_count
love_count = l_count + o_count + v_count + e_count

# Contatenate the strings
love_score = int(str(true_count) + str(love_count)) 

# Condition check for love_score
if (love_score > 10) or (love_score < 90):
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif (love_score >= 40) and (love_score <= 50):
    print(f"Your love score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")