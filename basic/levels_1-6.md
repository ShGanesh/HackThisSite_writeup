## Level 1
Pretty basic.  
Inspect the page and scroll away.  
Also, you should at least know about HTML before attempting further missions.  

## Level 2
Also, pretty basic.  
Since he forgot to upload the password file the value of password is naturally NULL.  
Just submit NULL.  

## Level 3
`<input type="hidden" name="file" value="password.php">`  

Go to :   
> https://www.hackthissite.org/missions/basic/3/password.php  

## Level 4  
`<input type="hidden" name="to" value="sam@hackthissite.org">`  
`<input type="submit" value="Send password to Sam">`

Since this value is manipulable just type your email address in value.

## Level 5  
Similar to Level 4... strange bt worked for me...

## Level 6  
On trying the string "lllll" it spat back "lmnop". So we can now understand its logic. Try it yoursels! You can do it by hand **or** by code.  
The code (in python) would look like:   
```
st = "lllll"
ans = ""
for i in range(len(st)):      
    ans += chr(ord(st[i])+i)      # Increasing ASCII value by the character's position in the string.  
print(ans)
```
> Output: lmnop     

So its reverse would be:
```
st = lmnop
ans = ""
for i in range(len(st)):
    ans += chr(ord(st[i])-i)      # Decreasing ASCII value by the character's position in the string.   
print(ans)
```
> Output: lllll   

You can use this Code but try to make one on your own. ***Google*** is your best friend!
