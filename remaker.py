from json import load, dump

with open('verbs.json' ,'r') as verbs:
    data = load(verbs)

    new_json = {"verbs": []}

    for verb in data:
        new_json["verbs"].append({"a":str(verb['Base'])

        })
    with open('test.json','w') as test:
        dump(new_json, test)




"""
"jeden": f'{verb["Base"]}',
"dwa": f'{verb["Past-simple"]}"',
"trzy": f'{verb["Past-Participle"]}'
"""