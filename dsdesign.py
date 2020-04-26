import re


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.wordList = []

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        self.wordList.append(word)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        result = False

        r = re.compile(word)
        newlist = list(filter(r.match, self.wordList))

        if len(newlist) > 0:
            result = True

        return result


# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
word = "bad"
obj.addWord(word)
param_2 = obj.search("b..")
print(param_2)

