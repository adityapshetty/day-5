import random
import urllib.request
words=[]
with urllib.request.urlopen("https://raw.githubusercontent.com/adityapshetty/day-5/main/listdoc.txt") as file:
    for line in file:
        i=line.strip()#strips \n and  \r
        i=str(i).strip("b")
        i=str(i).strip("'")
        words.append(i)
#above code is to create the list
temp=words.copy()
word = random.choice(words)
trials = len(words)
top=0
topscorer='none'
while True:
    name = input("Please enter your name:")
    print("Guess the words  ")
    j=0
    for i in range(0,trials):
        guess=input("enter your guess else use 0 to stop:")
        if guess in words:
            j+=1
            print(f"sucessesful\nfound {j},{trials-j} left\n{trials-i-1} trials left")
            words.remove(guess)
        elif(guess=='0'):
            break
        else:
            print(f"try again\n{trials-i-1} trials left")
    #the code below is to show the top scorer
    if j>top:
        top=j
        topscorer=name
    print(f"top scorer:{topscorer} score:{top}")
    words=temp.copy()
    h=input("press 0 to exit anything else to continue:")
    if '0'==h:
        break
