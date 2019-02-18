from string import maketrans as m
def to_rna(dna_strand):
	t = dna_strand
	dna = 'GCTA'
	rna = 'CGAU'
	a = m(dna,rna)
	return t.translate(a)













 
