from ChainingHashTableMap import *


class InvertedFile:
    def __init__(self, file_name):
        file = open(file_name, 'r')
        text = file.read().lower()
        file.close()
        for punctuation in "!?,.:;":
            text = text.replace(punctuation, '')
        word_bank = text.split()
        self.ht = ChainingHashTableMap()
        for i in range(len(word_bank)):
            if word_bank[i] in self.ht:
                self.ht[word_bank[i]].append(i)
            else:
                self.ht[word_bank[i]] = [i]

    def indices(self, word):
        if word in self.ht:
            return self.ht[word]
        return []


def main():
    inv_file = InvertedFile("row your boat.txt")
    inv_file.indices("row")
    # [0, 1, 2, 18, 19, 20]
    inv_file.indices("the")
    # [7, 25, 37]
    inv_file.indices("done")
    # []
