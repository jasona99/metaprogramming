def partial(func, *pargs, **kwargs):
    #def_kwargs = kwargs
    #def_pargs = pargs
    def the_returner(*pargs2, **kwargs2):
        return func(*pargs, *pargs2, **kwargs, **kwargs2)
    return the_returner


def sum(*args, **kwargs):
  out = 0
  for i in args:
    out += i
  for i in kwargs.values():
    out += i
  return out

p = partial(sum, 5)
print(p(3))
pp = partial(p, keyword=10)
print(pp(2))
