import argparse
import re

def read_gff(filename, feature):
	features = {}
	with open(filename) as fp:
		while True:
			line = fp.readline()
			if line == '': break
			f = line.split()
			chrom = f[0]
			beg = int(f[3]) -1
			end = int(f[4]) -1
			ftype = f[2]
			if ftype != feature: continue
			if chrom not in features: features[chrom] = []
			features[chrom].append( (beg, end) )
	return features

def read_fasta(filename):
	label = None
	seq = []
	with open(filename) as fp:
		while True:
			line = fp.readline()
			if line == '': break
			line = line.rstrip()
			if line.startswith('>'):
				if len(seq) > 0:
					seq = ''.join(seq)
					yield(label, seq)
					label = line[1:]
					seq = []
				else:
					label = line[1:]
			else:
				seq.append(line)
	yield(label, ''.join(seq))
	fp.close()


parser = argparse.ArgumentParser(
	description='Mask sequences with features')
parser.add_argument('fasta', type=str, metavar='<fasta>',
	help='fasta file')
parser.add_argument('gff', type=str, metavar='<gff>',
	help='gff file')
parser.add_argument('feature', type=str, metavar='<feature>',
	help='type of feature, e.g. CDS')
parser.add_argument('--lower', action='store_true',
	help ='use lowercase [default is N]')
arg = parser.parse_args()

features = read_gff(arg.gff, arg.feature)

for name, seq in read_fasta(arg.fasta):
	chrom = re.search('^\S+', name).group(0)
	if arg.lower: seq = seq.upper()
	aseq = list(seq)
	if chrom not in features: continue
	for beg, end in features[chrom]:
		for i in range(beg, end+1):
			if arg.lower: aseq[i] = aseq[i].lower()
			else:         aseq[i] = 'N'
	print(f'>{name}')
	for i in range(0, len(aseq), 80):
		line = ''.join(aseq[i:i+80])
		print(line)
