def toss():
 print("type '0' for head and '1' for tails ")
 t = int(input())
 if (t == random.randint(0, 1)):
  print(name, " have won the toss")
  print("type bat for batting and bowl for bowling")
  b = input()
  if (b == "bat"):
   batf()
  elif (b == "bowl"):
   bowlf()
  else:
   print("ur chance over")
   toss()
 else:
   print(name, " have loss the toss")
   if (random.randint(0, 1) == 0):
    print(name, " have to bowl first")
    bowlf()
   else:
    print(name, " have to bat first")
    batf()


def batf():
 a=0
 for i in range(0, 60, 1):
  b=int(input("{}:".format(name)))
  if (0 <= b) and (b <= 6):
   if (b == random.randint(0, 6)):
    print(x + name, "got out")
    break
   else:
    a=a+b
  else:
   print(x + "how can u hit more than 6 runs a ball")
 print(y + name, " scored: ", a)
 print(y + name, " total score is:", a)
 target = a + 1
 print(name, "has set", target, "as target")
 bowls(target)


def bowls(target):
 for i in range(0, 60, 1):
  b = int(input( "{}:".format(name)))
  if (0 <= b) and (b <= 6):
   p = random.randint(0, 6)
   if (p == b):
    print("com got out")
    break
   else:
    rem =target-b
    if (rem > 0):
     print("com has to score", rem)
    else:
     break
  else:
   print("use numbers 0 to 6")
 if (rem > 0):
   print(name, "has won the match")
 else:
   print("com has won the match")
   print("wanna play again type yes or no")
   o = input()
   if (o == "yes"):
    toss()
   else:
    print("thank you")


def bowlf():
 a=0
 for i in range(0, 60, 1):
  b = int(input( "{}:".format(name)))
  if (0 <= b) and (b <= 6):
   p = random.randint(0, 6)
   if (p == b):
    print("com got out")
    break
   else:
    a = a + p
  else:
   print("choose num between 0 to 6")
 print("com scored: ", a)
 print("com total score is:", a)
 target = a + 1
 print("com has set", target, "as target")
 bats(target)


def bats(target):
 for i in range(0, 60, 1):
  b = int(input( "{}:".format(name)))
  if (0 <= b) and (b <= 6):
   if (b == random.randint(0, 6)):
    print(x + name, "got out")
    break
   else:
    rem = target - b
    if (rem > 0):
     print(name, "has to score", rem)
    else:
     break
  else:
   print(x + "how can u hit more than 6 runs a ball")
 print(y + name, "have to score: ", rem)
 if (rem > 0):
   print("com has won the match")
 else:
   print(name, "has won the match")
 print("wanna play again type yes or no")
 o = input()
 if (o == "yes"):
  toss()
 else:
  print("thank you")


import random
a=0
rem=0
i = 0
x = '\033[31m'
y = '\033[32m'
z = '\033[34m'
w = '\033[33m'
print(w + "welcome to hand cricket")
print("enter ur name :")
name = input()
print(z + "type start' to play")
m = input()
if (m == "start"):
    toss()
else:
    print(w + "thank you")
