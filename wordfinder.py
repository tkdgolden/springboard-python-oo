from random import choice



class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, file):
        "creates a word finder object"

        self.word_list = self.__read_file__(file)
        print(f"{len(self.word_list)} words read")

    def __read_file__(self, file):
        "reads line by line of the file into a list"

        file = open(file)
        word_list = []
        for line in file:
            line = line.strip('\n')
            word_list.append(line)
        file.close
        return word_list
    
    def random(self):
        "returns a random word from the list"
        return choice(self.word_list)
    
class SpecialWordFinder(WordFinder):
    "extends WordFinder, filters empty lines and # lines"

    def __init__(self, file):
        "same init, but will call new read_file"

        super().__init__(file)

    def __read_file__(self, file):
        "checks that a line isnt empty or #commented -- doesn't include these in the list"

        file = open(file)
        word_list = []
        for line in file:
            line = line.strip('\n')
            if (line != "" and not line.startswith("#")):
                word_list.append(line)
        file.close
        return word_list
