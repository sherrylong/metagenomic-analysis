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

    def write(self, path):
        w = open(path, 'w')
        for kmer in self.mg_kmers:
            w.write(kmer + '\n')
        w.close()

    def build(self, path):
        w = open(path, 'w')
        for path in self.g_paths:
            w.write(path + ' ')
        w.write('\n')
        for mg_kmer in self.mg_kmers:
            for g_kmer_dict in self.g_kmers:
                if (mg_kmer in g_kmer_dict):
                    w.write('1 ')
                else:
                    w.write('0 ')
            w.write('\n')
        w.close()


    def print_all(self):
        # print("GENOMES")
        # for path in self.g_paths:
        #     print(path)
        # print("GENOME KMERS")
        # for kmer in self.g_kmers:
        #     print(kmer)
        # print()
        print("METAGENOMES")
        for path in self.mg_paths:
            print(path)
        print("METAGENOME KMERS")
        print(self.mg_kmers)