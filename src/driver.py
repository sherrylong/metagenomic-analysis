from color_matrix import *

cm = ColorMatrix({"test_data/test_gen_1.txt"}, {"test_data/test_mgen_1.txt"})
cm.count_genome_kmers(3)
cm.count_metagenome_kmers(3)
cm.print_all()