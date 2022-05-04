from abc import ABC, abstractmethod


class Word(ABC):
    @abstractmethod
    def __int__(self, word):
        self.word = word

    @abstractmethod
    def check_word(self):
        pass


class WordInInfinitive(Word):
    def __int__(self, word):
        self.word = word

    def check_word(self):
        pass




