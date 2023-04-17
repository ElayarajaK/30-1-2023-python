import json

person_json = '''{
    "name":"Raja",
    "country":"India",
    "city":"Chennai",
    "skills":["Python", "Java","R"]
}''';
print(type(person_json))
person_dct = json.loads(person_json)
print(type(person_dct))
print(person_dct)
print(person_dct['name'])

print("Done")