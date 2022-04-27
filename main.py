from json import load
from abc import abstractmethod, ABC





with open('verbs.json') as verbs:
    data = load(verbs)
    print((data['verbs']))



dict = {"test":[
    {'a':'a'},
    {'b':'b'},
    {'c':'c'}
]}
if __name__ == "__main__":

    print(len(dict['test']))