group = [{"name": "Kelvin", "age": 45},
         {"name": "John", "age": 65},
         {"name": "Gift", "age": 85}]

print(sorted(group, key=lambda i: i["name"]))

print(sorted(group, key=lambda i: i["age"]))

print(sorted(group, key=lambda i: (i["age"], i["name"])))