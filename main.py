from json import load
from abc import abstractmethod, ABC





with open('verbs.json') as verbs:
    data = load(verbs)
    print((data['verbs']))

