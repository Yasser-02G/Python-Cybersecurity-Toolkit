import marshal

with open('scripte.py', 'r', encoding='utf-8') as file:
    code = file.read()


en_code = marshal.dumps(compile(code, '<string>','exec'))

with open('new.py','wb') as file:
    file.write(en_code)

print('Done ! ')