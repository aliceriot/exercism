
def distance(dna1, dna2):
    hamming = 0

    for i in range(len(dna1)):
        if dna1[i] != dna2[i]:
            hamming += 1

    return hamming

