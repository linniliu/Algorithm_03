# BASKET PROBLEM
# You are given two lists which give you the weight and the value of things.
# The basket has a max weight it can carry.
# Your job is to fill the basket with the highest value of things, as long as it can hold the weight.
# You want to maximize the value. You can use unlimited values of each.

# Creating empty lists to allow user to input a list of steps skipped
weight = []
value = []
max_weight = 0

# Filling the lists based on user inputs
weight_input = int(input("Please enter the total number of weights, followed by their corresponding weights: "))
value_input = int(input("Please enter the total number of values, followed by their corresponding values: "))
max_weight_input = int(input("What is the maximum allowed weight? "))

# Creation of the weight and value lists base on previous user inputs
for w in range(0, weight_input):
    weight_input = int(input())
    weight.append(weight_input)

for v in range(0, value_input):
    value_input = int(input())
    value.append(value_input)


