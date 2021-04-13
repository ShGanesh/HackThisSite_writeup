answers = []                        # Initializing an empty list


def bits2string(b=None):            # Function to convert 8 by 8 binary strings to strings
    return ''.join([chr(int(x, 2)) for x in b])


def mod(x):                         # Function for inserting 0 at each place of the binary string one by one
    for i in range(0, len(x)):
        c = ''
        c += x[:i]
        c += "0"
        c += x[i:]
        div(c)


def div(s):                         # Divide up the big binary string into 8 by 8 chunks
    if len(s) == 8*7:               # Won't work if there are less bytes would it?
        l = []
        for i in range(0, 8*7, 8):
            l.append(s[i:i+8])
        answers.append(bits2string(l))
    else:
        print("Inadequate len", len(s))


# Main

hexes = "16 16 16 17 17 17 16 17 ..."   # Paste the hex codes here
ans = ""

for i in tuple(hexes.split(" ")):       # Convert Hex to 0 and 1
    if i == "16":
        ans += "0"
    else:
        ans += "1"
`
if len(ans) == 55:
    mod(ans)

for e in set(answers):
    print(e)
    
    
