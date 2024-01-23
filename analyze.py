''' Papa Yaw Owusu Nti
    September 28th, 2023
    CS 152 B
    Project 03
    this program reads a datafile, prints the header line and splits the rest of the columns into a list.
    It then casts the items in a user specified column into a float and uses imported libary stat 
    to compute the sum, mean, variance, max, min, max_index and min_dex 
    of the column specified by the user through the commandline of a datafile. The column is
    specified by the user through the command line using the imported library sys
'''
import sys
import stats
import stats_extension
def main(filename, column_id):
    '''    this main function reads a datafile, prints the header line and splits the rest of the columns into a list.
    It then casts the items in a user specified column into a float and uses imported libary stat 
    to compute the sum, mean, variance, max, min, max_index and min_dex 
    of the column specified by the user through the commandline of a datafile. The column is
    specified by the user through the command line using the imported library sys'''
    
# assign to fp the result of opening the file hurricanes.csv for reading
    fp= open(filename, "r")
# assign to line the first line of the data file
    line= fp.readline()
# assign to headers the result of splitting the line using commas
    headers =line.split(",")
# print headers
    print(headers)
# assign to a list variable named data an empty list
    data=[]
# for all of the remaining lines in the file
# assign to items the result of splitting the line using commas
    for line in fp:
        items = line.split(',')
        # append the second item cast as a float to data (which index?
        data.append(float(items[column_id]))
        
    # close the data file
    fp.close()
    # print data
    print(data)
    
    #computing statistics of data by importing statspy
    print(f'the sum of the data is {stats.sum(data)}')
    print(f'The mean of the data is {stats.mean(data):.2f}')
    print(f'the variance of the data is {stats.variance(data):.2f}')
    print(f'the minimum of the data is {stats.min(data)}')
    print(f'the maximum of the data is {stats.max(data)}')
    print(f'the minimum index of the data is {stats.min_index(data)}')
    print(f'the maximimum index of the data is {stats.max_index(data)}')  
    
    #extension
    print(f'Using my extension module, the standard deviation of the data is {stats_extension.standard_dev(data)}')   
    
if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]))
