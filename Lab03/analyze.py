''' Papa Yaw Owusu Nti
    September 28th, 2023
    CS 152 B
    Lab 03
'''
import sys
import stats
def main(filename, column_id):
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
    print(stats.sum(data))
if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]))
