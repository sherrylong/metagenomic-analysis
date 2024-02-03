from random import random

class SyntheticGenerator:
    read_paths = list()
    write_path = str()

    def __init__(self, read_paths, write_path):
        self.read_paths = read_paths
        self.write_path = write_path
    
    def add_genome(self, path):
        self.read_paths.append(path)
    
    def generate(self):
        w = open(self.write_path, 'w')
        for path in self.read_paths:
            with open(path) as f:
                seq = f.readline() # skips header in read
                while seq:
                    seq = f.readline().strip() # extracts line in read
                    if ((int(random()*10)+1) % 4 == 0 and len(seq) != 0): # 20% chance of inclusion
                        w.write('@fasta header\n') # writes header
                        w.write(seq + '\n') # writes line
        w.close()
