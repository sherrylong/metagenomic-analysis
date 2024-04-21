import random

class ColorMatrix:
    g_paths = list()
    mg_paths = list()
    g_kmers = dict()
    g_lists = list()
    g_sets = dict()
    g_reduced_sets = dict()
    mg_kmers = dict()
    matrix = dict()
    reduced_matrix = dict()

    def __init__(self, g_paths, mg_paths):
        self.g_paths = g_paths
        self.mg_paths = mg_paths
        self.g_lists = [0] * len(self.g_paths)

    def add_genome(self, g_path):
        self.g_paths.append(g_path)
    
    def add_metagenome(self, mg_path):
        self.mg_paths.append(mg_path)

    def count_genome_kmers(self, k):
        for p in range(len(self.g_paths)):
            path = self.g_paths[p]
            with open(path) as f:
                line = f.readline() # skips header
                while line:
                    line = f.readline().strip() # extracts line
                    if (line == '' or line[0] == '>'):
                        continue
                    for i in range(len(line)+1-k):
                        seq = line[i:i+k] # extracts k-mer
                        # seq = seq[0:int(k/4)]+seq[int(3*k/4):] # reduces k-mer
                        if (seq in self.g_kmers): 
                            self.g_kmers[seq][p] = True
                        else:
                            self.g_kmers[seq] = [False] * len(self.g_paths) 
                            self.g_kmers[seq][p] = True
    
    def count_metagenome_kmers(self, k):
        for path in self.mg_paths:
            with open(path) as f:
                line = f.readline() # skips header
                while line:
                    line = f.readline().strip() # extracts line
                    for i in range(len(line)+1-k):
                        seq = line[i:i+k] # extracts k-mer
                        # seq = seq[0:int(k/4)]+seq[int(3*k/4):] # reduces k-mer
                        if (seq in self.mg_kmers):
                            self.mg_kmers[seq] = self.mg_kmers[seq] + 1 # counts frequency of k-mer
                        else:
                            self.mg_kmers[seq] = 1
                    line = f.readline() # skips header

    def build_g_sets(self):
        added = False
        for mg_kmer in self.mg_kmers:
            if (mg_kmer in self.g_kmers): 
                row = self.g_kmers[mg_kmer]
                key = tuple(row)
                if key in self.g_sets:
                    self.g_sets[key].add(mg_kmer)
                else:
                    self.g_sets[key] = set()
                    self.g_sets[key].add(mg_kmer)

    def build_reduced_sets(self):
        for i,key in enumerate(self.g_sets):
            self.g_reduced_sets[key] = set()
            size = max(1, int(0.01 * len(self.g_sets[key]))) # Set the desired size for reduced sets to 1% of the original set size
            g_sets_as_list = list(self.g_sets[key])
            
            # print(i/len(self.g_sets))

            for index in range(size):
                self.g_reduced_sets[key].add(g_sets_as_list[index])


    def build_reduced_matrix(self):
        index = 0
        for key in self.g_sets:
            if key not in self.reduced_matrix:
                self.reduced_matrix[index] = key
                index += 1

    def build(self):
        for mg_kmer in self.mg_kmers:
            if (mg_kmer in self.g_kmers): # checks presence of k-mer in genome and excludes k-mers present in all genomes
                row = self.g_kmers[mg_kmer]
                if (False in row):
                    self.matrix[mg_kmer] = row

    def write_kmers(self, path): # writes metagenome k-mers to file
        w = open(path, 'w')
        for kmer in self.mg_kmers:
            w.write(kmer + '\n')
        w.close()
    
    def write_kmers_with_sets(self, path):
        w = open(path, 'w')
        i = 1
        for key in self.g_sets:
            w.write("GROUP " + str(i) + " - " + str(key) + '\n')
            for kmer in self.g_sets[key]:
                w.write(kmer + '\n')
            w.write(" " + '\n')
            i += 1
        w.close()
    
    def write_kmers_with_sets_reduced(self, path):
        w = open(path, 'w')
        i = 1
        for key in self.g_reduced_sets:
            w.write("GROUP " + str(i) + " - " + str(key) + '\n')
            for kmer in self.g_reduced_sets[key]:
                w.write(kmer + '\n')
            w.write(" " + '\n')
            i += 1
        w.close()

    def write_matrix(self, path): # writes color matrix to file
        w = open(path, 'w')
        for path in self.g_paths:
            w.write(path + ' ')
        w.write('\n')
        for row in self.matrix.values():
            for num in row:
                w.write(str(int(num)) + ' ')
            w.write('\n')
        w.close()
    
    def write_reduced_matrix(self, path): # writes color matrix to file
        w = open(path, 'w')
        for path in self.g_paths:
            w.write(path + ' ')
        w.write('\n')
        for row in self.reduced_matrix.values():
            for num in row:
                w.write(str(int(num)) + ' ')
            w.write('\n')
        w.close()

    def write(self, path):
        # self.write_kmers(path + '_kmers.txt')
        self.write_kmers_with_sets(path + '_kmers.txt')
        self.write_kmers_with_sets_reduced(path + '_reduced_kmers.txt')
        self.write_matrix(path + '_matrix.txt')
        self.write_reduced_matrix(path + '_reduced_matrix.txt')

    def test(self):
        for i in range(len(self.g_paths)):
            print(self.g_paths[i])
            total = 0
            for row in self.g_kmers.values():
                total += row[i]
            count = 0
            for row in self.matrix.values():
                count += row[i]
            print('Count: ' + str(count))
            print('Total: ' + str(total))
            print('Percentage: ' + str(count/total))