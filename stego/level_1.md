
# HackThisSite-> Stego
## Level 1

Download the file and open it in your favourite hex editor.  
*Hint: This is an encoded message, the only tip you get is '2 null bytes'*  

Null bytes are... "`00`" (without the quotation marks),  
Search in the hex editor: "`00 00`"  

In one part you will see something like this:  
>    "2d 3r 00 16 16 17 17 17 16 16 17 ... 17 00 6e f1"

We can observe that there are many **16**s and **17**s between the two `00`.  
Let **16** correspond to 0 and **17** correspond to **1** *(because come on they look like binaries)*. You can use the .py code in this directory.

After the Hex have been converted into binary, Try it in an online Hex-to-Text converter.
Wrong answer?
Divide the whole binary string into chunks of 8 and try again.



Woah we seem to be missing one character somewhere...
Should we try inserting a 0 or a 1 in the code arbitrarily? Nah we are not machines. We Automate Stuff!!!

Attept it yourself first. If you don't understand try visiting the level_1.py that is in this directory to understand my procedure.

*In bytes there is a concept of bit significance, where the last (or first) bit of a byte is kknown to be of least significance. You can try modification there.*


If you used my code you will get many potential answers. Try them out!
 
