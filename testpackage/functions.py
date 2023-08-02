
def string_function(s:str) -> str:
    new_s = ""
    for n, c in enumerate(s):
        nc = ""
        if n%2==0:
            nc = c.upper()
        else:
            nc = c.lower()
        new_s += nc
    return new_s

