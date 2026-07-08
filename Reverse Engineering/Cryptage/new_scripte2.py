import marshal
import dis

with open('new_scripte1.pyc','rb') as file:
    file.seek(16)
    de_code = marshal.loads(file.read())

code_str = dis.code_info(de_code)
print(code_str)
