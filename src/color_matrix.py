class ColorMatrix:
    g_paths = list()
    mg_paths = list()
    g_kmer_dict = dict()
    mg_kmer_dict = dict()
    g_kmers = set()
    mg_kmers = set()
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
            with open(path) as f:
                line = f.readline() # skips header
                while line:
                    line = f.readline().strip() # extracts line
                    for i in range(len(line)+1-k):
                        seq = line[i:i+k] # extracts k-mer
                        if (seq in self.g_kmer_dict): 
                            self.g_kmer_dict[seq] = self.g_kmer_dict[seq] + 1 # counts frequency of k-mer
                        else:
                            self.g_kmer_dict[seq] = 1
    
    def count_metagenome_kmers(self, k):
        for path in self.mg_paths:
            with open(path) as f:
                line = f.readline() # skips header
                while line:
                    line = f.readline().strip() # extracts line
                    for i in range(len(line)+1-k):
                        seq = line[i:i+k] # extracts k-mer
                        if (seq in self.mg_kmer_dict):
                            self.mg_kmer_dict[seq] = self.mg_kmer_dict[seq] + 1 # counts frequency of k-mer
                        else:
                            self.mg_kmer_dict[seq] = 1
                    line = f.readline() # skips header


    def print_all(self):
        print("GENOMES")
        for path in self.g_paths:
            print(path)
        print("GENOME KMERS")
        for kmer in self.g_kmers:
            print(kmer)
        print()
        print("METAGENOMES")
        for path in self.mg_paths:
            print(path)
        print("METAGENOME KMERS")
        for kmer in self.mg_kmers:
            print(kmer)