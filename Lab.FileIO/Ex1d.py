with open('names.txt', 'r') as file_obj:
   names = file_obj.readlines()
print(list(names).join())
print(f'There are {len(names)} names')
