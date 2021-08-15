import re

string = "helloworld"

regex01 = 'hello(world)'
regex02 = '(hello(world))'

res_01 = re.findall(regex01, string)
res_02 = re.findall(regex02, string)

print(res_01)
print(res_02)