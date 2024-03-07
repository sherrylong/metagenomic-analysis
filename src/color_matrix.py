class ColorMatrix:
    g_paths = list()
    mg_paths = list()
    g_kmers = list()
    mg_kmers = dict()
    matrix = dict()

    def __init__(self, g_paths, mg_paths):
        self.g_paths = g_paths
        self.mg_paths = mg_paths

    def add_genome(self, g_path):
        self.g_paths.append(g_path)
    
    def add_metagenome(self, mg_path):
        self.mg_paths.append(mg_path)

    def count_genome_kmers(self, k):
        for path in self.g_paths:
            kmers = dict()
            with open(path) as f:
                line = f.readline() # skips header
                while line:
                    line = f.readline().strip() # extracts line
                    if (line == '' or line[0] == '>'):
                        continue
                    for i in range(len(line)+1-k):
                        seq = line[i:i+k] # extracts k-mer
                        if (seq in kmers): 
                            kmers[seq] = kmers[seq] + 1 # counts frequency of k-mer
                        else:
                            kmers[seq] = 1
                self.g_kmers.append(kmers)

    
    def count_metagenome_kmers(self, k):
        for path in self.mg_paths:
            with open(path) as f:
                line = f.readline() # skips header
                while line:
                    line = f.readline().strip() # extracts line
                    for i in range(len(line)+1-k):
                        seq = line[i:i+k] # extracts k-mer
                        if (seq in self.mg_kmers):
                            self.mg_kmers[seq] = self.mg_kmers[seq] + 1 # counts frequency of k-mer
                        else:
                            self.mg_kmers[seq] = 1
                    line = f.readline() # skips header

    def build(self):
        for mg_kmer in self.mg_kmers:
            row = list() 
            for g_kmer_dict in self.g_kmers:
                if (mg_kmer in g_kmer_dict): # checks presence of k-mer in genome
                    row.append(1)
                else:
                    row.append(0)
            self.matrix[mg_kmer] = row # stores row with k-mer as key

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
                w.write(str(num) + ' ')
            w.write('\n')
        w.close()

    def write(self, path):
        self.write_kmers(path + '_kmers.txt')
        self.write_matrix(path + '_matrix.txt')

    def test(self):
        total = len(self.matrix.values())
        for i in range(0, len(self.g_paths)):
            print(self.g_paths[i])
            count = 0
            for row in self.matrix.values():
                count += row[i]
            print('Count: ' + str(count))
            print('Total: ' + str(total))
            print('Percentage: ' + str(count/total))
            