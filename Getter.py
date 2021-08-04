
def Printer(s):
    if("debuginfo" in s):
        product = s[0:s.find("debuginfo") - 1]
        s = s[s.find("debuginfo") + 10 : ]
        version = s[: s.find('-')]
        print(product)
        print(version)
    return 0

s = ["neko-debuginfo-17.0-salada","neko17.0-salada"]
print(s)
for index in enumerate(s):
    Printer(index[1])
