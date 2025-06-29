score=0
print("Welcome to our Quiz")
inputs=input("Do you want to play the Quiz ")

if inputs.lower()=="yes":
    print("Ok I will Start the Quiz ")
else:
    quit()

print("who was the president of India")
a=input("")
if a.lower()=="narendra modi":
    print("Correct !!")
    score+=1
else:
    print("Incorrect !!")


print("RAM stands for")
b=input("")
if b.lower()=="random access memory":
    print("Correct !!")
    score+=1
else:
    print("Incorrect !!")

print("CPU stands for")
c=input("")
if c.lower()=="central processing unit":
    print("Correct !!")
    score+=1
else:
    print("Incorrect !!")

print("JDBC stands for")
d=input("")
if d.lower()=="java database connectivity":
    print("Correct !!")
    score+=1
else:
    print("Incorrect !!")


print("JDK stands for")
e=input("")
if e.lower()=="java development kit":
    print("Correct !!")
    score+=1
else:
    print("Incorrect !!")


print("JRE stands for")
f=input("")
if f.lower()=="java runtime environment":
    print("Correct !!")
    score+=1
else:
    print("Incorrect !!")


print(f"you gave {score} correct answers out of 6\nyour score is {score}")
print(f"you got {(score/6)*100}%")

 

