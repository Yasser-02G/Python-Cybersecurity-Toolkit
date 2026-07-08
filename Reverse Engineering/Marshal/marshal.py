import marshal

code = input("entrer votre code : ")

# Cryptage

en_code = marshal.dumps(compile( code ,'<string>','exec'))
print(f"code encrypted : {en_code}")

# Encryptage

de_code = marshal.loads(en_code)
exec(de_code)