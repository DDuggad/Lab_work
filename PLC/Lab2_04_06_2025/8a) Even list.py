input_list = input("Enter numbers separated by spaces: ").split()

#Convert the input strings to integers
original_list=[]
even_list=[]

for num in input_list:
    num=int(num) #Convert the current number to an integer
    original_list.append(num) #Add the number to the original list
    if num%2==0:
        even_list.append(num) #Add the number to the even list if it's even

#Output the original and even number lists
print("Original list: ", original_list)
print("List of even numbers: ",even_list)
