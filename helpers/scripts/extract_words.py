import time
from pathlib import Path

wordLength = 6
fileName = "six-letter-words"

# finds words that are of the desired length
# creates a .txt file with all of the words in /valid-words
def extractWords() -> int:
    start = time.time()
    here = Path(__file__).parent
    textFolderPath = here.parent.parent/"valid-words"
    
    # open a new file for writing
    with open(textFolderPath / (fileName + ".txt"), "w") as output_file:
        # read the file line by line
        with open(textFolderPath/"scrabble-word-list.txt") as file:
            for line in file:
                # find only the words that have the correct length (expected length + 1) for white space
                if len(line) == wordLength + 1:
                    output_file.write(line)

    end = time.time()
    print("Function Time:", (end-start))
    

extractWords()