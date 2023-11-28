from random import random

class MetagenomeGenerator:
    paths = list()
    genome = str()

    def __init__(self, paths):
        self.paths = paths
    
    def add_genome(self, path):
        self.paths.append(path)
    
    def generate(self):
        not_first_line = False
        for path in self.paths:
            with open(path) as f:
                w = open("test_data/test_mgen_2.txt", "w")
                seq = f.readline()
                while seq:
                    seq = f.readline().strip()
                    if ((int(random()*10)+1) % 3 == 0 and len(seq) != 0): # 30% chance of inclusion
                        if not_first_line: w.write("\n@fasta header\n")
                        else: 
                            w.write("@fasta header\n")
                            not_first_line = True
                        w.write(seq)
        w.close()
