# BIO439finalexam
# Genome Sequence Analysis
This script analyzes genome fragments by identifying k-mer of a specified length, as well as their subsequent substrings

## Usage
### get_kmers(k, sequence)
This function extracts k-mers of length 'k' from the given sequence and outputs possible subsequent substrings for each k-mer

### get_smallest_k(sequence)
This function identifies the smallest value of k where every substring has only one possible substring that follows it

### process_sequences(file_path, k)
This function identifies all possible substrings and their subsequent substrings for all sequences read from a file

## Necessary Software
Python3
