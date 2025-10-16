names = input("Enter First Names separated by space: ").split()
ages = input("Enter Respective Age separated by space: ").split()
combine_lists = dict(zip(names, ages))
print("Combined Lists into dictionary (Names and Ages):\n",combine_lists)
