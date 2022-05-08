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
        return data.pop()

    def check_word(self):
        self.get_words()
        infinitive = self.get_words()['Infinitive']
        past_simple = self.get_words()['Past Simple']
        past_participle = self.get_words()['Past Participle']

