def wrap_with(f):
    return lambda s: (f(s), s)
    
def rank(unsorted):
    letters = { 'A': 0, 'C': 0, 'G': 0, 'T': 0 }
    difference = 0
    
    for character in unsorted:
        letters[character] += 1
        
    for character in unsorted:
        if character == 'A':
            letters['A'] -= 1
        elif character == 'C':
            letters['C'] -= 1
            difference += letters['A']
        elif character == 'G':
            letters['G'] -= 1
            difference += letters['A'] + letters['C']
        elif character == 'T':
            letters['T'] -= 1
            difference += letters['A'] + letters['C'] + letters['G']
        else:
            raise Exception("unknown sequence")
    
    return difference    

    

    
elems = [
    "TTTTGGCCAA",
    "CCCGGGGGGA",
    "TTTGGCCAAA",
    "GATCAGATTT",
    "AACATGAAGT",
    "ATCGATGCAT",
]

for score, str in sorted(map(wrap_with(rank), elems)):
    print(str, score )