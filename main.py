from json import load
from random import shuffle, randint
from abc import abstractmethod, ABC


class Word:
    def __init__(self, file: str):
        self.file = file

    def get_words(self):
        with open(self.file, 'r') as file:
            data = load(file)
            shuffle(data)
        return data.pop[0]

    def check_word(self):
        self.get_words()
        infinitive = self.get_words()['Infinitive']
        past_simple = self.get_words()['Past Simple']
        past_participle = self.get_words()['Past Participle']



class Game:
    pass


with open('inregular_verbs.json') as verbs:
    data = load(verbs)
    print(type(data))
    shuffle(data)
    print(len(data))
    print(data)
    p = data.pop(0)
    print(p[ 'Past Participle'])



# if __name__ == "__main__":

