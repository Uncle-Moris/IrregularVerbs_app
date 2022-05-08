from words import Word

def test_ss():
    test_word = Word('inregular_verbs.json')
    assert len(test_word.get_words()) == 3