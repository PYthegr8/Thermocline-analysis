''' Papa Yaw Owusu Nti
    September 28th, 2023
    CS 152 B
    Lab 03
'''
def sum(numbers):
# Create a variable to hold the sum
# Initialize the variable to 0.0 (explicitly make it a floating point number).
    sum_numbers = 0.0
# Define a for loop to iterate over the list passed in as the function parameter. 
    for x in numbers:
        # On each iteration, add the current number to the variable holding the sum. 
        sum_numbers+= x
    return sum_numbers

        # Once the loop completes, return the sum.
    
    
def test():
    list1 = [1,2,3,4]
    list2 = sum(list1)
    print(list2)

if __name__ == "__main__":
    test()

