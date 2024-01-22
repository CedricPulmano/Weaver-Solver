from pathlib import Path
from helpers.TrieStructure import Trie

wordLengthFiles = {
    4: "four-letter-words.txt",
    5: "five-letter-words.txt"
}

# add all words of the same length to a trie
def addWordsToTrie(wordLength: int):
    here = Path(__file__).parent
    wordsFilePath = here.parent/"valid-words"/wordLengthFiles[wordLength]

    words = Trie()

    with open(wordsFilePath) as file:
        for line in file:
            words.insertWord(line.strip())

    return words
