from color_matrix import *
from synthetic_gen import *

mg = SyntheticGenerator([], '../data_out/synthetic_2.txt')
mg.add_genome('../data/Clostridium botulinum.fna')
mg.add_genome('../data/Clostridium septicum.fna')
mg.add_genome('../data/Escherichia coli.fna')
mg.add_genome('../data/Salmonella enterica.fna')
mg.generate()

cm = ColorMatrix([], ['../data_out/synthetic_2.txt'])
cm.add_genome('../data/Clostridium botulinum.fna')
cm.add_genome('../data/Clostridium septicum.fna')
cm.add_genome('../data/Escherichia coli.fna')
cm.add_genome('../data/Salmonella enterica.fna')
cm.count_genome_kmers(50)
cm.count_metagenome_kmers(50)
cm.write('../data_out/synthetic_2_kmers.txt')
cm.build('../data_out/synthetic_2_matrix.txt')

def test():
    mg = MetagenomeGenerator([], "../test_out/test_syn_1")
    mg.add_genome("../test_data/test_gen_1.txt")
    mg.add_genome("../test_data/test_gen_2.txt")
    mg.add_genome("../test_data/test_gen_3.txt")
    mg.generate()

    cm = ColorMatrix([], ["../test_out/test_syn_1"])
    cm.add_genome("../test_data/test_gen_1.txt")
    cm.add_genome("../test_data/test_gen_2.txt")
    cm.add_genome("../test_data/test_gen_3.txt")
    cm.count_genome_kmers(3)
    cm.count_metagenome_kmers(3)
    cm.write("../test_out/test_syn_1_kmers.txt")
    cm.build("../test_out/test_syn_1_matrix.txt")