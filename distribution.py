"""
distribution.py
Author: Katie Naughton
Credit: I worked alone. 

Assignment:

Write and submit a Python program (distribution.py) that computes and displays 
the distribution of characters in a given sample of text.

Output of your program should look like this:

Please enter a string of text (the bigger the better): The rain in Spain stays mainly in the plain.
The distribution of characters in "The rain in Spain stays mainly in the plain." is:
iiiiii
nnnnnn
aaaaa
sss
ttt
ee
hh
ll
pp
yy
m
r

Notice about this example:

* The text: 'The rain ... plain' is provided by the user as input to your program.
* Uppercase characters are converted to lowercase
* Spaces and punctuation marks are ignored completely.
* Characters that are more common appear first in the list.
* Where the same number of characters occur, the lines are ordered alphabetically. 
  For example, in the printout above, the letters e, h, l, p and y both occur twice 
  in the text and they are listed in the output in alphabetical order.
* Letters that do not occur in the text are not listed in the output at all.
"""
text1=input("Please enter a string of text (the bigger the better): ")
print('The distribution of characters in "'+text1+'" is: ')

text=text1.lower()

letlist=[]
for i in "abcdefghijklmnopqrstuvwxyz":
    count=text.count(i)
    if count>0:
        letlist.append(count*i)
#print(letlist)

freqlist=[]
for i in "abcdefghijklmnopqrstuvwxyz":
    count=text.count(i)
    if count>0:
        freqlist.append(count)
#print(freqlist)

comblist=list(zip(freqlist, letlist))
comblist.sort()
#print(comblist)

for n in range(len(comblist),-1, -1):
    for c in comblist:
        if c[0]==n:
            print(c[1])
            
#CONVERT UPPERCASE TO LOWERCASE
    
    
    





    


