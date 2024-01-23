''' Papa Yaw Owusu Nti
    October 4th, 2023
    CS 152 B
    Lab 03
    This program computes the density and the thermocline_depth of a list of data
'''

import stats

def density(temps):
    '''Calculate and return the density from a list of temperatures'''
    density_list =[]
# Calculate density for each temperature and append to the list    
    for t in temps:
        rho = 1000 * (1 - (t + 288.9414) * (t - 3.9863)**2 / (508929.2*(t + 68.12963)))
        density_list.append(rho)
    return density_list

def thermocline_depth( temps, depths ):
    '''Calculate and return the thermocline depth from a list of temperatures'''
    
    # assign to rhos the result of calling the density function with temps as the argument
    # create an empty list named drho_dz – these are the derivatives of the density
    rhos = density(temps)
    drho_dz =[]
    
    for i in range(len(rhos)-1):
        # loop for one less than the length of rhos
        # append to drho_dz  the quantity rhos[i+1] minus rhos[i] divided by the quantity depths[i+1] minus depths[i]
    	# optional step: print out temps[i], rhos[i], and drho_dz[i]
        compute_deriv= (rhos[i+1] - rhos[i])/ (depths[i+1] -depths[i])
        drho_dz.append(compute_deriv)
        # print (temps[i])
        # print (rhos[i])
        # print (drho_dz[i])
          
        # assign to max_drho_dz the the result of calling the max function in stats.py with drho_dz as the argument
	    # assign to maxindex the result of calling the max_index function in stats.py with drho_dz as the argument
        max_drho_dz=  stats.max(drho_dz)
        maxindex = stats.max_index(drho_dz)
        
        # compute thermoDepth by taking the average of depths[ maxindex ] and depths[ maxindex+1]
        
        thermoDepth = (depths[maxindex]+ depths[maxindex+1])/ 2
    return thermoDepth  
  
