from bwt_structures import *
from compsci260lib import *
from future.backports.misc import count

def find(query, bwt_data):
    """
    Given a query sequence and a series of data structures
    containing various information about the reference genome,
    return a list containing all the locations of the query
    sequence in the reference genome. 
    """
    
    bwt, suffix_array, ranks, counts = bwt_data
      
    length = len(bwt)
    results = []
#     print bwt
#     print suffix_array
#     print ranks
#     print counts
    """YOUR CODE GOES HERE..."""
    """
    Reverse the query sequence to facilitate the iterative steps. The first part
    is to initialize the s and e parameters, which represent the start index and 
    end index of the range of rows respectively.
    """
    re_query = query[::-1]
    s = counts[re_query[0]] + 1
    e = counts[re_query[0]] + ranks[re_query[0]][-1]
#     s = 1
#     e = length - 1
    """
    Following is the iterative steps to update the s and e index.
    """
    for j in range(1,len(re_query)):
        s = counts[re_query[j]] + ranks[re_query[j]][s-1] + 1
        e = counts[re_query[j]] + ranks[re_query[j]][e]
        if s > e: # situation that query sequence cannot be found in the ref seq
            break
    if s <= e:
        for k in range(s, e + 1, 1):
            results.append(suffix_array[k])
        return sorted(results)
    else:
        return results
    
if __name__ == '__main__':
    # example query sequence
    query_sequence = "AAACGA"
    # example reference sequence
    sequence = "AAAAAAAAACGATAGAGA"
#     query_sequence = 'AGC'
#     sequence = 'AGCAACG'
#     sequence = 'AGCAGCAGC'
    print 'The positon list for the given example is:', find(query_sequence, make_all(sequence))
