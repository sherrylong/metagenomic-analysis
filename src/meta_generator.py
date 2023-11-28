from random import random

class MetagenomeGenerator:
    paths = list()
    genome = str()

    def __init__(self, paths):
        self.paths = paths
    
    def add_genome(self, path):
        self.paths.append(path)
    
    def generate(self):
        for path in self.paths:
            with open(path) as f:
                seq = f.readline()
                while seq:
                    seq = f.readline()
                    if ((int(random()*10)+1) % 3 == 0 and len(seq) != 0): # 30% chance of inclusion
                        self.genome += "@fasta header\n"
                        self.genome += seq
        self.genome = self.genome.strip()
        return self.genome
