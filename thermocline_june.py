''' Papa Yaw Owusu Nti
    October 9th, 2023
    CS 152 B
    Lab 03
    This program computes the density and the thermocline_depth for June 2019
'''


import thermocline


def main():
    ''' This function computes the density and the thermocline_depth for June 2019 
    by keeping track of the number of days and writing the computation into a new file  thermo_depths_june.csv'''
	# these are the fields corresponding to the temperatures in order by depth
	# note they use 0-indexing
    fields = [10, 11, 16, 17, 15, 14, 13, 12]
	# these are the depth values for each temperature measurement
    depths = [ 1, 3, 5, 7, 9, 11, 13, 15 ]
 
    # open the data file and read past the header line
    fout = open("Goldie2019June.csv","r")
    fout.readline()
    day= 0
    fp = open("thermo_depths_june.csv","w")
    fp.write("day,depth" + "\n")

    for line in fout:
        words = line.split(",")
        if "12:03:00 PM" in words[0]:
            day+=1
            temps =[]
            for i in range(len(depths)):
                temps.append(float(words[fields[i]]))
            thermo_depth = thermocline.thermocline_depth(temps,depths)
            fp.write( str(day) + "," + str(thermo_depth) + "\n")         
  
  
    fp.close()
    fout.close()
      		
if __name__ == "__main__":
	main()


