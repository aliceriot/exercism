
def to_rna(dna_string):
    translate = {'C': 'G', 'G': 'C', 'T': 'A', 'A': 'U'}
    rna = ''.join(list(map(lambda c: translate[c], dna_string.upper())))
    
    return rna
        
