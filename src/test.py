from color_matrix import *
from synthetic_gen import *

mg = SyntheticGenerator(['../data/Bacillus mycoides.fna',
                         '../data/Bacillus paranthracis.fna', 
                         '../data/Bacillus safensis.fna',
                         '../data/Bacillus subtilis.fna',
                         '../data/Bacillus thuringiensis.fna'], '../data_out/synthetic_3.txt')
mg.generate()

cm = ColorMatrix(['../data/Bacillus mycoides.fna',
                '../data/Bacillus paranthracis.fna', 
                '../data/Bacillus safensis.fna',
                '../data/Bacillus subtilis.fna',
                '../data/Bacillus thuringiensis.fna',
                '../data/Bacillus licheniformis.fna',
                '../data/Bacillus cereus.fna',
                '../data/Bacillus cabrialesii.fna',
                '../data/Bacillus anthracis.fna'], ['../data_out/synthetic_3.txt'])

cm.count_genome_kmers(50)
cm.count_metagenome_kmers(50)
cm.build()
cm.write('../data_out/synthetic_3')
cm.test()