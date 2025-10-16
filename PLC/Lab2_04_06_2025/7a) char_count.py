#input string from the user
string= input("Enter a string: ").lower().strip()

#initialize an empty dictionary to store character counts
char_count = {}

#iterate through each character in the string
for char in string:
    #use the get method to get the current count of the character, defaulting to 0
    char_count[char]=char_count.get(char,0)+1

#Print the resulting dictionary
print("Character count: ",char_count)
