class ColorMatrix:
    g_paths = list()
    mg_paths = list()
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
                seq = f.readline()
                while seq:
                    seq = f.readline().strip()
                    for i in range(len(seq)+1-k):
                        self.g_kmers.add(seq[i:i+k])
    
    def count_metagenome_kmers(self, k):
        for path in self.mg_paths:
            with open(path) as f:
                seq = f.readline()
                while seq:
                    seq = f.readline().strip()
                    for i in range(len(seq)+1-k):
                        self.mg_kmers.add(seq[i:i+k])
                    seq = f.readline()


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