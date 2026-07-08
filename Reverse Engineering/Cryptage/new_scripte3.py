import marshal
import dis


with open('new_scripte1.pyc', 'rb') as f :
    f.seek(16)
    de_code = marshal.loads(f.read())

dis.dis(de_code)
print(de_code)