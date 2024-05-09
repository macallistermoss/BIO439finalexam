def get_kmers(k, sequence):
    #extract substring of length k (kmer)
    kmer = sequence[0:k]
  
    substring_counts = {}
  
    #loop over sequence and extract substring of length k from every possible starting place 
    for i in range(len(sequence) - k + 1):
        #define kmers as sequences that are k values away from any starting point 
        kmers = sequence[i:i + k]
        print("K-mer:", kmers)
    
        #get all possible substrings of each kmer
        for letter in ['A', 'T', 'G', 'C']:
            substring = kmers[1:] + letter
            print("Subsequent substring:", substring)
            
            #if the substring is not in the dictionary, add it and set count to 1
            if substring not in substring_counts:
                substring_counts[substring] = 1
            else:
                #if the substring is already in the dictionary, increase its count
                substring_counts[substring] += 1

    return substring_counts  
    
# Define genome sequence
sequence = "ATGTCTGTCTGAA"
# Define length of kmers
k = 2
print("Sequence:", sequence)
print("K-mers and Unique Substrings:")
print(get_kmers(k, sequence))


#Define a function to identify all possible substrings and their subsequent substrings for all sequences read from a file
def process_sequences(file_path, k):
  #open file
  with open(file_path, 'r') as file:
    #read file 
    sequences=file.readlines()
  
  #iterate over each sequence   
  for line, sequence in enumerate(sequences):
    print("Sequence", line +1)
    print("K-mers and Unique Substrings:")
    print(get_kmers(k, sequence.strip()))
    

#Define a function to identify the smallest value of k where every substring has only one possible substring that follows it
def get_kmers(k, sequence):
    #extract substring of length k (kmer)
    kmer = sequence[0:k]
    
    #create dictionary for substrings
    substring_counts = {}
  
    #loop over sequence and extract substring of length k from every possible starting place 
    for i in range(len(sequence) - k + 1):
        #define kmers as sequences that are k values away from any starting point 
        kmers = sequence[i:i + k]
        print("K-mer:", kmers)
    
        #get all possible substrings of each kmer
        for letter in ['A', 'T', 'G', 'C']:
            substring = kmers[1:] + letter
            print("Subsequent substring:", substring)
            
            #if the substring is not in the dictionary, add it and set count to 1
            if substring not in substring_counts:
                substring_counts[substring] = 1
            else:
                #if the substring is already in the dictionary, increase its count
                substring_counts[substring] += 1

    return substring_counts

def get_smallest_k(sequence):
    #start from k=2
    for k in range(2, len(sequence)):
        #create a set to store unique substrings
        unique_substrings = set()
        for i in range(len(sequence) - k):
            kmer = sequence[i:i+k]
            next_substring = sequence[i+1:i+k+1]
            #add substring to set
            unique_substrings.add((kmer, next_substring))
        #check if substring only occurs once    
        if all(sum(1 for pair in unique_substrings if pair == (kmer, next_substring)) == 1 for kmer, next_substring in unique_substrings):
            return k
    #if no k value for only one possible substring, return none
    return None

sequence = "ATGTCTGTCTGAA"
print("Sequence:", sequence)
smallest_k = get_smallest_k(sequence)
print("Smallest k value:", smallest_k)
print("K-mers and Unique Substrings:")
print(get_kmers(smallest_k, sequence))
