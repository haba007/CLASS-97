from itertools import count


name=7
print(name)
a=input("Enter your name")
print(a)
b=4

if b ==4:
    print("two numbers are equal")

elif b>=4:
    print("b>4")

string=input ("enter string ")
correctorcount =0
wordCount=1
for i in string:
    correctorcount=correctorcount+1
    if( i=="  "):
          wordCount=wordCount+1
print("number of words in string")
print(wordCount)        
print (correctorcount)