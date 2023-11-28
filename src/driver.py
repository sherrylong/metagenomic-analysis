from color_matrix import *
from meta_generator import *

mg = MetagenomeGenerator({"test_data/test_gen_1.txt"})
print(mg.generate())

'''
cm = ColorMatrix({"test_data/test_gen_1.txt"}, {"test_data/test_mgen_1.txt"})
cm.count_genome_kmers(3)
cm.count_metagenome_kmers(3)
cm.print_all()
'''