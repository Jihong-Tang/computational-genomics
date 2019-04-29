import sys, random
from compsci260lib import *
from math import exp

def simulate():
    """YOUR CODE GOES HERE..."""
    """
    Create a function called seq_process to simulate the sequencing process one time,
    taking the input parameters G(whole genome length), R(number of reads), L(length
    of each read). The output is a count list with G numbers to record the sequencing 
    situation on each position in the whole genome sequence.
    """
    def seq_process(G,R,L):
        result_list = [0] * G
        for i in range(R):
            start = random.randint(0,G-L)
            for j in range(L):
                result_list[start+j] += 1
        return result_list
    
    """
    Create a function called sti_process to do the simulation procedure multiple 
    times. Output is a dictionary which contains the number will be used to compute
    in the following questions.
    """
    def sti_process(G,R,L,times):
        result_dict = {}
        for item in ['empirical coverage', 'number of not covered nucleotide', 
                     'number of contigs', 'average contig lenth']:
            result_dict[item] = []

        for i in range(times):
            print "It is simulation process No.%d, total times is %d" % (i + 1, times)
            result_list = seq_process(G, R, L)[L-1:G-L+1]# address the edge effects
            length = len(result_list)
            compare_list = [1 if e != 0 else 0 for e in result_list]
            result_str = ''.join(str(e) for e in compare_list)
            
            result_dict['empirical coverage'].append(sum(result_list)/length)
            
            zero_list = re.findall('0', result_str)
            not_seq = len(zero_list)
            result_dict['number of not covered nucleotide'].append(not_seq)
            
            contig_list = re.findall('[^0]0', result_str)
            end = 0 if result_list[-1] == 0 else 1 
            num_contig = len(contig_list) + end
            result_dict['number of contigs'].append(num_contig)
            
            result_dict['average contig lenth'].append((length - not_seq)/num_contig)
        return result_dict
    """
    Create a function called ave_result to print out the average result after multiple
    times' simulation work. The input is the result dictionary containing all results
    from each simulation procedure. 
    """
    def ave_result(result_dict):
        key = result_dict.keys()
        length = len(result_dict[key[0]])
        for item in key:
            print 'The %s for total 20 stimulations are shown in the list below:' % item
            print result_dict[item]
            ave = sum(result_dict[item])/ length
            print 'The average of %s for total 20 stimulations is: %d' % (item, ave)
    
    ave_result(sti_process(3000000, 40000, 450, 20))

if __name__ == '__main__':
    simulate()