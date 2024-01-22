from pathlib import Path
from helpers.word_length_file_map import wordLengthFiles

# add all words of the same length to a set
def addWordsToSet(wordLength: int):
    here = Path(__file__).parent
    wordsFilePath = here.parent/"valid-words"/wordLengthFiles[wordLength]

    words = set()

    with open(wordsFilePath) as file:
        for line in file:
            words.add(line.strip())

    return words
