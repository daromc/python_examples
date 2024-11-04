# dario romo program.
# ask the user his name
name = input("What is your first name and last name : ")
#strip method  remove white space from star and end
name = name.strip()
#capitalize the users name
name = name.title()
#split the first name and last name
first, last  = name.split(" ")

#use two methods use => name.strip().title()
# say hello to user.
print("hello, " + name)
#second form to print with format file
print(f"hello, {first} {last}")
