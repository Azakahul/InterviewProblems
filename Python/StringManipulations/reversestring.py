def reverseloop(s):
    str = ""
    for i in s:
        str = i + str
    return str


def reverserecur(s):
    if len(s) == 0:
        return s
    else:
        return reverserecur(s[1:] + s[0])