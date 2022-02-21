# Multiple return inside function

def format_name(f_name, l_name):
    '''Takes first and last name and format it to 
    returns the title case of formatted string'''
    if f_name=="" or l_name=="":
        return "Didn't provide valid inputs."
    name = f_name.title() + " " + l_name.title()
    return name

print(format_name(input("What is your first name? "), input("What is your last name?")))

