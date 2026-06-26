def to_rna(dna_strand):
    RNA = ''
    for nucleotide in dna_strand:
        if nucleotide == 'G':
            RNA += 'C'
        elif nucleotide == 'C':
            RNA += 'G'
        elif nucleotide == 'T':
            RNA += 'A'
        elif nucleotide == 'A':
            RNA += 'U'

    return RNA
