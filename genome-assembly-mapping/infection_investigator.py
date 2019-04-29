#coding:utf-8
from bwt_structures import *
from read_aligner import *
from compsci260lib import *

def reverse_complement(seq):
    """
    Returns the reverse complement of the input string.
    """
    comp_bases = {'A': 'T',
                  'C': 'G',
                  'G': 'C',
                  'T': 'A'} 
    rev_seq = list(seq)
    rev_seq = rev_seq[::-1]
    rev_seq = [comp_bases[base] for base in rev_seq] 
    return ''.join(rev_seq)
    
def align_patient_reads():
    """YOUR CODE GOES HERE..."""
    """Create a dictionary called ref_dict to input all reference bacterial fasta file
    """
    ref_dict = {}
    ref_name = ['Bacteroides_ovatus','Bacteroides_thetaiotaomicron','Biﬁdobacterium_longum',
                'Eubacterium_rectale', 'Lactobacillus_acidophilus', 'Peptoniphilus_timonensis',
                'Prevotella_copri', 'Roseburia_intestinalis', 'Ruminococcus_bromii','Vibrio_cholerae']
    for item in ref_name:
        read_dict = get_fasta_dict('reference_genomes/%s.fasta'% item)
        ref_dict.update(read_dict)
    ref_keys = ref_dict.keys()
    ref_keys.sort()
    
#     for key in ref_keys:
#         ref_dict[key] = reverse_complement(ref_dict[key])
    
    """Create a dictionary called ref_fm_dict to store all data　structure needed 
    to make the fm-index procedure for all ten reference genomes
    """
    ref_fm_dict = {}
    for key in ref_keys:
        ref_fm_dict[key] = make_all(ref_dict[key])
    patient1_dict = get_fasta_dict('patients/patient1.fasta')
    patient2_dict = get_fasta_dict('patients/patient2.fasta')    
    patient3_dict = get_fasta_dict('patients/patient3.fasta')
    def find_prevalence(patient_dict):
        pkey = patient_dict.keys()
        result_dict ={}
        for key in ref_keys:
            result_dict[key] = 0
        for i in pkey:
            p_dict = {}
            p_dict[i] = []
            re_seq = reverse_complement(patient_dict[i])
#             re_seq = patient_dict[i]
            for j in ref_keys:
                result = find(re_seq, ref_fm_dict[j])
                if result != []:
                    p_dict[i].append(j)
            if len(p_dict[i]) == 1:
                result_dict[p_dict[i][0]] += 1
        return result_dict

    def cal_print_pre(patient_name, result_dict):
        total = 0
        for key in ref_keys:
            total += result_dict[key]
        for key in ref_keys:
            pre = float(result_dict[key]) / float(total) 
            print "The estimated prevalence of microbe %s for %s is %.2f%%." % (key, patient_name, pre*100)
        return 0
    
    print 'The estimated microbe prevalences for patient1 are shown as following:'
    cal_print_pre('patient1', find_prevalence(patient1_dict))
      
    print 'The estimated microbe prevalences for patient2 are shown as following:'
    cal_print_pre('patient2', find_prevalence(patient2_dict))
      
    print 'The estimated microbe prevalences for patient3 are shown as following:'
    cal_print_pre('patient3', find_prevalence(patient3_dict))
       
    def find_count(patient_dict, ref_genome_name):
        count_list = [0] * len(ref_dict[ref_genome_name])
        pkey = patient_dict.keys()
        read_length = len(patient_dict[pkey[0]])
        start_list = []
        for key in pkey:
            re_seq = reverse_complement(patient_dict[key])
            p_dict = {}
            p_dict[key] = []
            for j in ref_keys:
                result = find(re_seq, ref_fm_dict[j])
                if result != []:
                    p_dict[key].append(j)
            if p_dict[key] == [ref_genome_name]:
                start_list += find(re_seq, ref_fm_dict[ref_genome_name])
        for e in start_list:
            for i in range(read_length):
                count_list[e+i] += 1
        return count_list
#     print find_count(patient1_dict, 'Vibrio cholerae')[]
    def find_zeros(count_list):
        """
        In order to use the re function, I convert the count_list to count_str. 
        However, it will be an error if original mutation is taken since some number 
        in the count_list has more than one digit position, this will cause trouble 
        in the determination of position in string. Therefore, I firstly change all
        number which are not equal to zero to be one for convenience.
        """
        mut_list = [1 if e != 0 else 0 for e in count_list]
        count_str = ''.join(str(e) for e in mut_list)
#         print count_list
#         print mut_list
#         print count_str
        zeros = re.finditer('0+', count_str)
        max, opt = 0, 0
        for m in zeros:
            if m.start() !=0 and m.end()!= len(count_list):
                interval = m.end() - m.start()
                if interval > max:
                    max = interval
                    opt = m
        if opt != 0:
            return opt.start(), opt.end()
        else:
            return 'None continuous internal zeros can be found from the given information.','You may check your data.'
        
    start1, end1 = find_zeros(find_count(patient1_dict, 'Vibrio cholerae'))
    a = find_count(patient1_dict, 'Vibrio cholerae')[start1:end1]
    
    print 'After using the new hunch method on patient1, the 0-indexed start position of the longest internal string of 0s in genome Vibrio cholerae will be %d, and the 1-indexed end position will be %d.' %(start1, end1)
    start2, end2 = find_zeros(find_count(patient3_dict, 'Vibrio cholerae'))
    print 'The information can be worked out for patient3 is: %s %s' %(start2, end2)
#     print 'After using the new hunch method on patient3, the 0-indexed start position of the longest internal string of 0s in genome Vibrio cholerae will be %, and the 1-indexed end position will be % .' %(start2, end2)
    target_str = ref_dict['Vibrio cholerae'][start1:end1]
    print 'The target string found is: %s' % target_str

if __name__ == '__main__':
    align_patient_reads()
