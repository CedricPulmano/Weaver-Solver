from pathlib import Path

# add all alphabet letters to an array
def addLettersToArray():
    here = Path(__file__).parent
    alphabetFilePath = here.parent/"valid-words"/"alphabet.txt"
    
    alphabet = []

    with open(alphabetFilePath) as file:
        for line in file:
            alphabet.append(line.strip())
            
    return alphabet

