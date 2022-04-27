from json import load, dump

with open('verbs.json' ,'r') as verbs:
    data = load(verbs)

    new_json = {"verbs": []}
    n = 0

    for verb in data["verbs"]:
        new_json["verbs"].append({'Infinitive': verb['Base'],
                                 'Past Simple': verb['Past-simple'],
                                  'Past Participle': verb["Past-Participle"
                                  ] })
        n+=1

    print(new_json)

#    with open('test.json', 'w') as test:
#        dump(new_json, test)

