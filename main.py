from words import Word

while True:
    START = input("Co chcesz zrobić")

    if START == "OK":
        word = Word('inregular_verbs.json')

        words = word.get_words()
        while True:
            print(f'twoje słowo to {words["Infinitive"]}')
            word2 = input("Podaj 2 formę")
            if word2 == words['Past Simple']:
                print('bardzo dobrze')
                break
