my_file = open("data.txt", "r", encoding="utf-8")

lines = my_file.readlines()
print(lines)


my_file.close