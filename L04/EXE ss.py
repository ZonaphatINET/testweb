f_name = str(input("Enter your fires name: "))
l_name = str(input("Enter your last name: "))
s_id = str(input("Enter your stident ID number: "))
sy_login = (f_name[0:3]) + (l_name[0:3]) + (s_id[-3::])
print("Your system login name is: ",sy_login)