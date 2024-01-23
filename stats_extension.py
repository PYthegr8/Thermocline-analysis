''' Papa Yaw Owusu Nti
    October 11th, 2023
    CS 152 B
    Lab 03
    This extension program computes the standard deviation for a piece of data
'''

import stats

def standard_dev (data):
    '''This function computes the standard deviation for a piece of data.
    It first computes the variance of the data and finds the squareroot of this variance. It returns the value as a float'''
    #find variance of data
    var_data = stats.variance(data)
    
    #since standard deviation is the square root of variance. Also square root = a number to the power half
    st_dev_data = var_data ** 0.5
    return st_dev_data

#Testing the function
    
sample_data= [1,2,3,4,5]
sample_stdev = standard_dev(sample_data)
print(sample_stdev)

if __name__ == "__main__":
    standard_dev(sample_data)
