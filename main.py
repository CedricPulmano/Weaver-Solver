import time
from memory_profiler import profile
from queue import Queue
from typing import Set, List, Optional
from helpers.add_words_to_set import addWordsToSet
from helpers.add_letters_to_array import addLettersToArray

startingWord = "lost"
targetWord = "soul"

@profile
def main() -> Optional[List[str]]:
    start = time.time()
    
    # get data about the problem
    validWords = addWordsToSet(len(startingWord))
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
def exploreWord(queue: Queue[List[str]], visited: Set[str], validWords: Set[str], alphabet: List[str], targetWord: str) -> Optional[List[str]]:  
    # queue is empty; exhausted all options
    while not queue.empty():
        path = queue.get()
        word = path[-1]
        # print(word)
    
        # already tested
        if word in visited:
            continue
        # word not in word list
        if word not in validWords:
            continue
        # word matches targetWord
        if word == targetWord:
            return path
        
        visited.add(word)
        
        # search all possible words that are only one letter different from current word
        for s in range(len(word)):
            for letter in alphabet:
                newWord = word[:s] + letter + word[s+1:]
                newPath = path.copy()
                newPath.append(newWord)
                queue.put(newPath)
    
    # queue is empty, no results found
    return []
            
    
if __name__ == "__main__":
    main()