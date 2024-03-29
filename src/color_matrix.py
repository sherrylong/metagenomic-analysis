class ColorMatrix:
    g_paths = list()
    mg_paths = list()
    g_kmers = dict()
    g_lists = list()
    mg_kmers = dict()
    matrix = dict()

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

    def write(self, path):
        self.write_kmers(path + '_kmers.txt')
        self.write_matrix(path + '_matrix.txt')

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