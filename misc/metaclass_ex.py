# Comment computing ids:
'''
wjc3hg
jaa8r
sm5ve
zw6aw
jr6ff
dh8cd
afj3vh
jac3rd
abw9yd
mcb9sm
mem5ak
cjk8ad
asb7bp
iws4kc
dvc8bg
dra4ae
jy2gm
gmf5de
bak9cu
hf6mw
hbh3re
ekb6ee
cew8ut
pcb8gb
tm5me
mg2nf
'''


'''
@staticmethod

'''

class Statifier(type):
    def __new__(meta, name, bases, attrs):
        for key in attrs:
            if callable(attrs[key]):
                attrs[key] = staticmethod(attrs[key])
        return type.__new__(meta, name, bases, attrs)




class foo(metaclass=Statifier):
    var = 1
    def bar(a, b):
        pass

#Statifier.__new__('foo', (object,), {'bar': <function>, 'var' : 1})
