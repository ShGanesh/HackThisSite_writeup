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

## Level 7  
We can see that the system is very immature and uses UNIX.  
Let's try to list all files present in the present directory.  
Input: ```; ls```  
Semicolon used to end line, ls lists all files present in current directory.  
We can now see that after the calender there are a few other elements there:  
*index.php  
*level7.php
*cal.pl
*.
*..
*k1kh31b1n55h.php  

Nice, this k1something5h.php looks interesting.  
Try putting 'k1something5h' into the password. Does it work?   
So, go to   
> https://www.hackthissite.org/missions/basic/7/k1kh31b1n55h.php  

Done.

## Level 8  
Here too we can se that like the previous level we need to list all files in that directory.  
Let's try Input: ```; ls```   
>Output: Hi, ; ls! Your name contains 4 characters.  

But it takes the whole string as input rather than letting it break. What if we encapsulate the payload in a comment? Comments arent processed right?  
Let's Try Input: ```<!--; ls```>  
>Output: *If you are trying to use server side includes to solve the challenge, you are on the right track: but I have limited the commands allowed to ones >relevant towards finding the password file for security reasons(because there will always be that one person who decides to execute some rather nasty commands). >So please manipulate your code so that it is a little more pertaining to the level.*  

Let's Ask for help from out=r best friend ***Google***!   
Since the level hint hinted about SSI, we shall resecrh about it!  
Found: https://owasp.org/www-community/attacks/Server-Side_Includes_(SSI)_Injection  

Here we can see prebuilt commmands. Now trying 
Input: ```<!--#exec cmd="ls ../"-->``` 
> Output: Hi, austuffvc.php index.php level8.php tmp! Your name contains 39 characters.

Yay! We got the list of files here!
Now you know what to do!

