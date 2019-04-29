'''
@author: Jihong Tang
@date: 09/25/2018
@note:

'''

from compsci260lib import *

def solve_pebble():
    """Your code goes here..."""
    """
    Import the sample grid file and read the data into a 2D array.
    """
    f = open("grid.txt","r")
    data_array = []
    for fline in f:
        flist = fline.strip().split()
        for i in range(len(flist)):
            flist[i] = int(flist[i])
        data_array.append(flist)
    """
    Below are some own-created test sample.
    data_array = [[1,10,100,1000]]
    data_array = [[1,10,100,1000],[1000,100,10,1]]
    data_array = [[1000,100,10,1],[1000,100,10,1],[1,10,100,1000]]
    data_array = [[1000,500,900,600], [10,20,30,40],[200,1000,600,900]]
    """
    """
    Creating the comp_dict to store the compatible information between different 
    patterns. The patterns are listed as the same order in question 3a
    """
    comp_dict = {"pa":["pb","pc","pd","pe","pf","pg","ph"], "pb":["pa","pc","pd","pe","ph"],
                 "pc":["pa","pb","pd","pe","pf","pg"],"pd":["pa","pb","pc","pe","pg","ph"],
                 "pe":["pa","pb","pc","pd","pf"],"pf":["pa","pc","pe","ph"],"pg":["pa","pc","pd"],
                 "ph":["pa","pb","pd","pf"]}
    """
    Creating the pattern_dict to store the pattern information, I use 0 to represent
    not putting, and 1 to represent putting.
    """
    pattern_dict = {"pa":[0,0,0,0],"pb":[1,0,0,0],"pc":[0,1,0,0],"pd":[0,0,1,0],
                    "pe":[0,0,0,1],"pf":[1,0,1,0],"pg":[1,0,0,1],"ph":[0,1,0,1]}
    pattern = pattern_dict.keys()
    result_dict = {} # the final dict will be used and update each time after a 
    #new column's calculaton work.
    
    # set the initial value
    for i in pattern:
        result_dict[i] = 0 
    # store the information of column 1
    for i in pattern:
        for j in range(4):
            result_dict[i] = result_dict[i]+ data_array[0][j] * pattern_dict[i][j]
    
    # Do the iterative work like shown in 3b
    for i in range(1,len(data_array)):
        new_dict = {} # the new_dict is used to store the new column's information and update the result_dict
        for j in pattern:
            new_dict[j] = 0
        for j in pattern:
            new_col_value = 0
            for d in range(4):
                new_col_value = new_col_value + data_array[i][d] * pattern_dict[j][d]
            for k in comp_dict[j]:
                q = result_dict[k] + new_col_value
                new_dict[j] = q if q > new_dict[j] else new_dict[j]
        result_dict = new_dict
    """
    Finding out the final result from the result_dict.
    """
    final_result = 0
    for i in pattern:
        q = result_dict[i]
        final_result = q if q > final_result else final_result
    print "The maximum value of a valid placement for this smaple grid is: \n%d" %final_result

if __name__ == '__main__':
    solve_pebble()
