def get_kmers(k, sequence):
    # Extract substring of length k (kmer)
    kmer = sequence[0:k]
    print("K-mer:", kmer)
  
    substring_counts = {}
  
    # Loop over sequence and extract substring of length k from every possible starting place 
    for i in range(len(sequence) - k + 1):
        # Define kmers as sequences that are k values away from any starting point 
        kmers = sequence[i:i + k]
        print("K-mer:", kmers)
    
        # Get all possible substrings of each kmer
        for letter in ['A', 'T', 'G', 'C']:
            substring = kmers[1:] + letter
            print("Subsequent substring:", substring)
            
            # If the substring is not in the dictionary, add it and set count to 1
            if substring not in substring_counts:
                substring_counts[substring] = 1
            else:
                # If the substring is already in the dictionary, increase its count
                substring_counts[substring] += 1

    return substring_counts

def get_smallest_k(sequence):
    for k in range(2, len(sequence)):
        unique_substrings = set()
        for i in range(len(sequence) - k):
            kmer = sequence[i:i+k]
            next_substring = sequence[i+1:i+k+1]
            unique_substrings.add((kmer, next_substring))
        if all(sum(1 for pair in unique_substrings if pair == (kmer, next_substring)) == 1 for kmer, next_substring in unique_substrings):
            return k
    return None




sequence = "ATGTCTGTCTGAA"
print("Sequence:", sequence)
smallest_k = get_smallest_k(sequence)
print("Smallest k value:", smallest_k)
print("K-mers and Unique Substrings:")
print(get_kmers(smallest_k, sequence))
