from examfinal import *

def test_get_smallest_k():
  sequence1 = "ATGTCTGTCTGAA"
  assert get_smallest_k(sequence1) == 2

  sequence2 = "ATGATGATG"
  assert get_smallest_k(sequence2) == 3

  sequence3 = "AAA"
  assert get_smallest_k(sequence3) == None

  sequence4 = "ATG"
  assert get_smallest_k(sequence4) == None

def test_get_smallest_k_wrong():
  sequence1 = "ATGTCTGTCTGAA"
  assert get_smallest_k(sequence1) != 1

  sequence2 = "ATGATGATG"
  assert get_smallest_k(sequence2) != 2

  sequence3 = "AAA"
  assert get_smallest_k(sequence3) != 1

  sequence4 = "ATG"
  assert get_smallest_k(sequence4) != 2
  
  
