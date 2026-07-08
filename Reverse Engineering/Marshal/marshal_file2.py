import marshal

with open('new.py', 'rb') as file :
    de_code = marshal.loads(file.read())

with open('dec.py', 'w') as file :
    file.write(str(de_code))
