def is_number_in_list(ordered_list, number):
    """ Check if a given number is in the ordered list.
        Args:
        ordered_list(list): A list of numbers in ascending order.
        number (int/float): The number to check.
        Returns:
        bool: True if the number is in the list. False otherwise.
        """
    #Check if the number exists in the list
    result = number in ordered_list
    #Print the result
    print(result)
    return result

#Input the list from the user
input_list = input("Enter a list of numbers separated by spaces: ").split()
input_list = [int(num) for num in input_list] #Convert the input to integers

#Ensure the list is sorted
ordered_list = sorted(input_list)

#Input the number to check
number = int(input("Enter a number to check: "))

#Call the function and store the result
is_number_in_list(ordered_list,number)
