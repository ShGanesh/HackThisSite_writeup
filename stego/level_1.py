

def bits2string(b=None):
    return ''.join([chr(int(x, 2)) for x in b])


def mod(x):
    for i in range(0, len(x)):
        c = ''
        c += x[:i]
        c += "0"
        c += x[i:]
        div(c)


def div(s):
    if len(s) == 8*7:
        l = []
        for i in range(0, 8*7, 8):
            l.append(s[i:i+8])
        print(bits2string(l))
    else:
        print("Inadequate len", len(s))


# Main

hexes = "16 16 16 17 17 17 16 17 ..."  # Paste the hex codes here
ans = ""

for i in tuple(hexes.split(" ")):
    if i == "16":
        ans += "0"
    else:
        ans += "1"
`
if len(ans) == 55:
    mod(ans)
    
