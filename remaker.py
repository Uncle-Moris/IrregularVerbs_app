from json import load, dump

with open('verbs.json', 'r') as verbs:
    data = load(verbs)

    new_json = []

    for verb in data["verbs"]:
        new_json.append({'Infinitive': verb['Base'],
                        'Past Simple': verb['Past-simple'],
                      'Past Participle': verb["Past-Participle"]})


with open('inregular_verbs.json', 'w') as new_made_file:
    dump(new_json, new_made_file)


