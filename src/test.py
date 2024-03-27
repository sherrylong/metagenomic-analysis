from color_matrix import *
from synthetic_gen import *

mg = SyntheticGenerator({'../data/Bacillus mycoides.fna' : 0.5,
                         '../data/Bacillus paranthracis.fna' : 0.6, 
                         '../data/Bacillus safensis.fna' : 0.7,
                         '../data/Bacillus subtilis.fna' : 0.8,
                         '../data/Bacillus thuringiensis.fna' : 0.9}, '../data_out/synthetic_3.txt')
                         
mg.generate()
print('Generated synthetic metagenome')

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
print('Counted all genome k-mers')
cm.count_metagenome_kmers(50)
print('Counted metagenome k-mers')
cm.build()
print('Building color matrix')
# cm.write('../data_out/synthetic_3')
cm.test()