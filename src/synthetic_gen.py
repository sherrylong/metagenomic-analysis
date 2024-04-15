import random

class SyntheticGenerator:
    read_paths = dict()
    write_path = str()

    def __init__(self, read_paths, write_path):
        self.read_paths = read_paths # path : % coverage
        self.write_path = write_path
    
    def add_genome(self, path):
        self.read_paths.append(path)

    def gen_garbage(self, line_length): # generates 200 lines of random bases
        bases = ['A', 'T', 'G', 'C']
        garbage_string = ''
        for n in range(200):
            garbage_string += '@fasta header\n'
            for l in range(line_length):
                garbage_string += random.choice(bases)
            garbage_string += '\n'
        return garbage_string
    
    def generate(self):
        w = open(self.write_path, 'w')
        for path in self.read_paths:
            with open(path) as f:
                seq = f.readline() # skips header in read
                while seq:
                    seq = f.readline().strip() # extracts line in read
                    if (random.random() <= self.read_paths[path] and len(seq) != 0): # inclusion based on % coverage
                        w.write('@fasta header\n') # writes header
                        w.write(seq + '\n') # writes line
        w.write(self.gen_garbage(80)) 
        w.close()
