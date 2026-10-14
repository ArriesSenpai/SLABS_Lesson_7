#Author: SLABS SE

def get_user_info():
    first_name = input("Enter your first name: ")
    second_name = input("Enter your second name: ")
    last_name = input("Enter you last name: ")
    return(first_name, second_name, last_name)

full_name = get_user_info()
print("Your full name is: %s %s %s"%(full_name[0], full_name[1], full_name[2]))

