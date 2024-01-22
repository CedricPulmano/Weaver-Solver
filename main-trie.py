import time
from memory_profiler import profile
from queue import Queue
from typing import Set, List, Optional
from helpers.TrieStructure import Trie
from helpers.add_words_to_trie import addWordsToTrie
from helpers.add_letters_to_array import addLettersToArray

startingWord = "charge"
targetWord = "comedo"

@profile
def main() -> Optional[List[str]]:
    start = time.time()
    
    # get data about the problem
    validWords = addWordsToTrie(len(startingWord))
    alphabet = addLettersToArray()

    # set up data structures
    queue = Queue()
    visited = set()
    queue.put([startingWord])

    result = exploreWord(queue, visited, validWords, alphabet, targetWord)
            
    end = time.time()
    print("Function Time:", (end-start))
    print(result)
    
    return result
    

# search through all possibilities
def exploreWord(queue: Queue[List[str]], visited: Set[str], validWords: Trie, alphabet: List[str], targetWord: str) -> List[str]:  
    # queue is empty; exhausted all options
    while not queue.empty():
        path = queue.get()
        word = path[-1]
    
        # already tested
        if word in visited:
            continue
        # word matches targetWord
        if word == targetWord:
            return path
        
        visited.add(word)
        
        # search all possible words that are only one letter different from current word
        for s in range(len(word)):
            for letter in alphabet:
                newWord = word[:s] + letter + word[s+1:]
                # word not in word list
                if not validWords.searchWord(newWord):
                    continue
                newPath = path.copy()
                newPath.append(newWord)
                queue.put(newPath)
    
    # queue is empty, no results found
    return []
            
    
if __name__ == "__main__":
    main()