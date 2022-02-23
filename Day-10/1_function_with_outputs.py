# Function with output

f_name = input("Type your first name: ")
l_name = input("Type your last name: ")

name = ""
def format_name(f_name, l_name):
    name = f_name.title() + " " + l_name.title()
    return name

formatted_name = format_name(f_name, l_name)
print(formatted_name) 
