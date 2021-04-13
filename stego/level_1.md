
# HackThisSite-> Stego
## Level 1

Download the file and open it in your favourite hex editor.
*Hint: This is an encoded message, the only tip you get is '2 null bytes'*

Null bytes are... "00" (without the quotation marks)
Search in the hex editor: "00 00"

In one part you will see something like this:
>    "2d 3r 00 16 16 17 17 17 16 16 17 ... 17 00 6e f1"

We can observe that there are many 16s and 17s between the two 00.
Let 16 correspond to 0 and 17 correspond to 1 *(because come on they look like binaries)*. You can use this .py code for that.


`
a = "16 16 16 17 17 17 16 17"
ans = ""

for i in tuple(a.split(" ")):
    if i == "16":
        ans += "0"
    else:
        ans += "1"

print(ans)
`

The answer will be //To be completed
