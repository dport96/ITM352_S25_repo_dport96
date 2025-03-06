with open('names.txt', 'r') as file_obj:
   names = file_obj.read()
print(names)
print(f'There are {len(names.split("\n"))} names')
