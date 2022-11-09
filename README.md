Conserved Non-Coding Sequences in Model Organisms
=================================================

Goal: Develop a BLAST-based solution to finding CNS

+ Typical UNIX CLI
+ Written in Python
+ Program automatically runs BLAST and processes output
	+ Input
		+ Favorite genome sequences in FASTA format
		+ Favorite genome annotations in GFF3 format
	+ Pre-processing
		+ Remove known coding sequence
		+ Make sequences manageable in size (maybe)
	+ Alignment
		+ Index 'database' files
		+ Run BLASTN with optimal parameters on pairs of genoems
	+ Post-processing
		+ Identify conserved pairs
		+ Identify conserved families
	+ Output
		+ Something organized and intuitive


## Removing Coding Sequence ##

```
python3 feature_masker.py ../datacore/genome_celegans/1pct_elegans.fa ../datacore/genome_celegans/1pct_elegans.gff3
```
