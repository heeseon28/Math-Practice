from operators import *

exec("p = True")
exec("q = False")
print("When p is True and q is False")

ret = eval("not p")
print("not p is {}".format(ret))

ret = eval("p and q")
print("p and q is {}".format(ret))

ret = eval("p or q")
print("p or q is {}".format(ret))

# ret = eval("p xor q")
# print("p xor q is {}".format(ret))
# Syntax Error 출력 -> xor이 존재하지 않음

ret = eval("p implies q")
print("p implies q is {}".format(ret))