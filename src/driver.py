from color_matrix import *
from synthetic_gen import *

mg = SyntheticGenerator(['../data/Clostridium botulinum.fna',
                         '../data/Clostridium septicum.fna', 
                         '../data/Escherichia coli.fna'], '../data_out/synthetic_1.txt')
mg.generate()

cm = ColorMatrix(['../data/Clostridium botulinum.fna', 
                  '../data/Clostridium septicum.fna', 
                  '../data/Escherichia coli.fna', 
                  '../data/Salmonella enterica.fna'], ['../data_out/synthetic_1.txt'])
cm.count_genome_kmers(50)
cm.count_metagenome_kmers(50)
cm.build()
cm.write('../data_out/synthetic_1')

def test():
    mg = SyntheticGenerator(['../test_data/test_gen_1.txt', 
                              '../test_data/test_gen_2.txt', 
                              '../test_data/test_gen_3.txt'], "../test_out/test_syn_1.txt")
    mg.generate()

    cm = ColorMatrix(['../test_data/test_gen_1.txt', 
                      '../test_data/test_gen_2.txt', 
                      '../test_data/test_gen_3.txt'], "../test_out/test_syn_1.txt")
    cm.count_genome_kmers(3)
    cm.count_metagenome_kmers(3)
    cm.build()
    cm.write('../test_out/test_syn_1')