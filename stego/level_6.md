# HackThisSite-> Stego
## Level 4

Download the .png and look at its hex using your favourite hex editor.  

In .png files the Picture content starts with IHDR and ends with IEND (roughly, you should read about it for more accurate information).  
Anything after IEND (and a few bits after that) is basically useless and hence can be used for payloads.  

Just copy it.  

Since the payload ends with a `==` we can safely assume that it is in Base64.  
Just edcode it online.
