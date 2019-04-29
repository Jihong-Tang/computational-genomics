'''
@author: Jihong Tang 
@date: 09/24/2018

@note:
Thanks to my roommate Shenghong Zhao, he provides me some ideas about the divide
and conquer solution including how to combine the left part and right part using 
another function. He is a transfer junior CS student and not in the class COMPSCI
260.
'''

from compsci260lib import *
import timeit
import random

def similarity_brute_force(score_list):
    """Your code goes here..."""
    opt_sim = float("-inf")
    for i in range(len(score_list)):
        index = i
        q = 0
        for j in range(index, len(score_list)):        
            q += score_list[j]
            opt_sim = opt_sim if opt_sim > q else q
    return max(0, opt_sim)

def similarity_divide_conquer(score_list):
    """Your code goes here..."""
    if len(score_list) == 1:
        return score_list[0]
    else:
        start = 0
        end = len(score_list) - 1
        mid = (start + end) // 2
        left_list = score_list[:mid+1]
        right_list = score_list[mid+1:]
        left_max_sum = similarity_divide_conquer(left_list)
        right_max_sum = similarity_divide_conquer(right_list)
        crossing_max_sum = find_crossing_max(score_list, mid)
        return max(left_max_sum, right_max_sum, crossing_max_sum, 0)
def find_crossing_max(score_list, mid):
    start = 0 
    end = len(score_list) - 1
    sum_left_max = sum_right_max = float("-inf")
    left_temp = right_temp = 0
    for i in range(mid, start-1, -1):
        left_temp += score_list[i]
        sum_left_max = sum_left_max if sum_left_max > left_temp else left_temp
    for i in range(mid+1, end+1):
        right_temp += score_list[i]
        sum_right_max = sum_right_max if sum_right_max> right_temp else right_temp
    return sum_left_max + sum_right_max

def similarity_linear(score_list):
    """Your code goes here..."""
    MAX_INCLUDING_HERE = MAX_SO_FAR = 0
    for i in range(len(score_list)):
        MAX_INCLUDING_HERE = score_list[i] + max(0, MAX_INCLUDING_HERE)
        MAX_SO_FAR = MAX_INCLUDING_HERE if MAX_INCLUDING_HERE > MAX_SO_FAR else MAX_SO_FAR
    return MAX_SO_FAR

if __name__ == '__main__':
    """ You can use this to test the correctness of your code by using
    sample_list as an input to each function """

    sample_list = [2,-3,-4,4,8,-2,-1,1,10,-5]
    print "The following three values are the test results for my three algorithm implement program"
    print similarity_brute_force(sample_list)
    print similarity_divide_conquer(sample_list)
    print similarity_linear(sample_list)

    """ This part below is used to test the runtime of your code, an example is
    given below for brute force algorithm with a random list of length 100.
    You will have to measure the runtime of each algorithm on every input size
    given in the problem set. """

    """
    allowed_scores = [i for i in range(-10,11)]
    random_list = [random.choice(allowed_scores) for x in range(100)]
    bruteforce_runtime = timeit.timeit('similarity_brute_force(random_list)', setup="from __main__ import similarity_brute_force, random_list", number=1)
    """
    allowed_scores = [i for i in range(-10,11)]
    random_list_2 = [random.choice(allowed_scores) for x in range(100)]
    random_list_3 = [random.choice(allowed_scores) for x in range(1000)]
    random_list_4 = [random.choice(allowed_scores) for x in range(10000)]
    random_list_5 = [random.choice(allowed_scores) for x in range(100000)]
    random_list_6 = [random.choice(allowed_scores) for x in range(1000000)]
    random_list_7 = [random.choice(allowed_scores) for x in range(10000000)]
    random_list_8 = [random.choice(allowed_scores) for x in range(100000000)]
    """
    bruteforce algorithm time evaluating
    """
    bruteforce_runtime_2 = timeit.timeit('similarity_brute_force(random_list_2)' ,
                                       setup = "from __main__ import similarity_brute_force, random_list_2",
                                       number = 1)
    print 'The running time of brute force algorithm of length 100 is \n %f ' %bruteforce_runtime_2
    bruteforce_runtime_3 = timeit.timeit('similarity_brute_force(random_list_3)' ,
                                       setup = "from __main__ import similarity_brute_force, random_list_3",
                                       number = 1)
    print 'The running time of brute force algorithm of length 1000 is \n %f ' %bruteforce_runtime_3
    bruteforce_runtime_4 = timeit.timeit('similarity_brute_force(random_list_4)' ,
                                       setup = "from __main__ import similarity_brute_force, random_list_4",
                                       number = 1)
    print 'The running time of brute force algorithm of length 10000 is \n %f ' %bruteforce_runtime_4
    bruteforce_runtime_5 = timeit.timeit('similarity_brute_force(random_list_5)' ,
                                       setup = "from __main__ import similarity_brute_force, random_list_5",
                                       number = 1)
    print 'The running time of brute force algorithm of length 100000 is \n %f ' %bruteforce_runtime_5
     
    """
    divide and conquer algorithm time evaluating
    """
    DAC_runtime_2 = timeit.timeit('similarity_divide_conquer(random_list_2)' ,
                                       setup = "from __main__ import similarity_divide_conquer, random_list_2",
                                       number = 1)
    print 'The running time of divide and conquer algorithm of length 100 is \n %f ' %DAC_runtime_2
    DAC_runtime_3 = timeit.timeit('similarity_divide_conquer(random_list_3)' ,
                                       setup = "from __main__ import similarity_divide_conquer, random_list_3",
                                       number = 1)
    print 'The running time of divide and conquer algorithm of length 1000 is \n %f ' %DAC_runtime_3
    DAC_runtime_4 = timeit.timeit('similarity_divide_conquer(random_list_4)' ,
                                       setup = "from __main__ import similarity_divide_conquer, random_list_4",
                                       number = 1)
    print 'The running time of divide and conquer algorithm of length 10000 is \n %f ' %DAC_runtime_4
    DAC_runtime_5 = timeit.timeit('similarity_divide_conquer(random_list_5)' ,
                                       setup = "from __main__ import similarity_divide_conquer, random_list_5",
                                       number = 1)
    print 'The running time of divide and conquer algorithm of length 100000 is \n %f ' %DAC_runtime_5
    DAC_runtime_6 = timeit.timeit('similarity_divide_conquer(random_list_6)' ,
                                       setup = "from __main__ import similarity_divide_conquer, random_list_6",
                                       number = 1)
    print 'The running time of divide and conquer algorithm of length 1000000 is \n %f ' %DAC_runtime_6
    DAC_runtime_7 = timeit.timeit('similarity_divide_conquer(random_list_7)' ,
                                       setup = "from __main__ import similarity_divide_conquer, random_list_7",
                                       number = 1)
    print 'The running time of divide and conquer algorithm of length 10000000 is \n %f ' %DAC_runtime_7
    
    """
    linear algorithm time evaluating
    """
    linear_runtime_2 = timeit.timeit('similarity_linear(random_list_2)' ,
                                       setup = "from __main__ import similarity_linear, random_list_2",
                                       number = 1)
    print 'The running time of linear algorithm of length 100 is \n %f ' %linear_runtime_2
    linear_runtime_3 = timeit.timeit('similarity_linear(random_list_3)' ,
                                       setup = "from __main__ import similarity_linear, random_list_3",
                                       number = 1)
    print 'The running time of linear algorithm of length 1000 is \n %f ' %linear_runtime_3
    linear_runtime_4 = timeit.timeit('similarity_linear(random_list_4)' ,
                                       setup = "from __main__ import similarity_linear, random_list_4",
                                       number = 1)
    print 'The running time of linear algorithm of length 10000 is \n %f ' %linear_runtime_4
    linear_runtime_5 = timeit.timeit('similarity_linear(random_list_5)' ,
                                       setup = "from __main__ import similarity_linear, random_list_5",
                                       number = 1)
    print 'The running time of linear algorithm of length 100000 is \n %f ' %linear_runtime_5
    linear_runtime_6 = timeit.timeit('similarity_linear(random_list_6)' ,
                                       setup = "from __main__ import similarity_linear, random_list_6",
                                       number = 1)
    print 'The running time of linear algorithm of length 1000000 is \n %f ' %linear_runtime_6
    linear_runtime_7 = timeit.timeit('similarity_linear(random_list_7)' ,
                                       setup = "from __main__ import similarity_linear, random_list_7",
                                       number = 1)
    print 'The running time of linear algorithm of length 10000000 is \n %f ' %linear_runtime_7
    linear_runtime_8 = timeit.timeit('similarity_linear(random_list_8)' ,
                                       setup = "from __main__ import similarity_linear, random_list_8",
                                       number = 1)
    print 'The running time of linear algorithm of length 100000000 is \n %f ' %linear_runtime_8