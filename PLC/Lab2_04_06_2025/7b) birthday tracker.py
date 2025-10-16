#Dictionary to store birthdays
birthdays={ "Alice":"1995-05-10", "Bob":"2000-07-21", "Charlie":"1998-12-05", "Diana":"1993-03-15"}

#Display available names
print("Welcome to the Birthday Tracker!")
print("Available names:",",".join(birthdays.keys()))

#Input: Ask the user for a name
name = input("Enter a name to find their birthday: ").strip()

#Trace the birthday
if name in birthdays:
    birth_date = birthdays[name] #Get the birthday (e.g., "2000-07-21")
    year, month, day = birth_date.split("-") #Split into parts: year, month, day
    formatted_date = "/".join([day,month,year]) #Join to format as DD/MM/YYYY
    print(f"{name}'s birthday is on {formatted_date}")
else:
    print(f"Sorry, no birthday found for {name}")
