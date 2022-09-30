print("hello world")
name=input("What is your name ? :")
age=int(input(f"{name.title()}  how old are you ? :"))
if age < 24:
    print( f"Ohhh {name} I am older than you ")
elif age == 24:
    print("We have same age ")
else:
    print(f"{name} :You are older than me")
adress=input("Where are you from ? :")
gender=input( "Oh realy? Are you man or woman ?:")
man=input(("Do you have a girlfriend ? :" ))
woman=(("Do you have a boyfriend ? :"))
if gender == "man":
    print(man )
    if man =="yes":
        print("Oh good ") 
    elif man =="no":
        print(f"{name.title()} you are {age} years old but you still don't  have a girlfiend What a f*** bro?")

else:
    print(woman)
    if woman =="yes":
        print("Oh good ") 
    elif man=="no":
     print(f"{name.title()}, you are {age} years old but you still don't  have a boyfriend What a f*** sister?")

music=input("Do you want to listing to music :")
if music =="yes":
    print("https://youtu.be/BIH40QZFoWQ")
elif music =="no":
    print("OK")
