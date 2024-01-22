from pathlib import Path
from helpers.TrieStructure import Trie
from helpers.word_length_file_map import wordLengthFiles

# add all words of the same length to a trie
def addWordsToTrie(wordLength: int):
    here = Path(__file__).parent
    wordsFilePath = here.parent/"valid-words"/wordLengthFiles[wordLength]

    words = Trie()

    with open(wordsFilePath) as file:
        for line in file:
            words.insertWord(line.strip())

    return words
