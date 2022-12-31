import random
x = "y"
print('''
 ____  _            ____  _                 _       _
|  _ \(_) ___ ___  / ___|(_)_ __ ___  _   _| | __ _| |_ ___  _ __
| | | | |/ __/ _ \ \___ \| | '_ ` _ \| | | | |/ _` | __/ _ \| '__|
| |_| | | (_|  __/  ___) | | | | | | | |_| | | (_| | || (_) | |
|____/|_|\___\___| |____/|_|_| |_| |_|\__,_|_|\__,_|\__\___/|_|

''')
while x == "y":
    b=input("Enter your name: ")
    a = int(input("Your number from (1,2,3,4,5,6): "))
    c = random.randint(1,6)
    print("The value appear on the dice is: ",c)
    if c == 1 and c==a:
        print("congratulations")
        print("----------------")
        print("----------------")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
    elif c == 2 and c==a:
        print("congratulations")
        print("----------------")
        print("----------------")
        print("[ 0   ]")
        print("[     ]")
        print("[   0 ]")
    elif c == 3 and c==a:
        print("congratulations")
        print("----------------")
        print("----------------")
        print("[     ]")
        print("[0 0 0]")
        print("[     ]")
    elif c== 4 and c==a:
        print("congratulations")
        print("----------------")
        print("----------------")
        print("[0   0]")
        print("[     ]")
        print("[0   0]")
    elif c == 5 and c==a:
        print("congratulations")
        print("----------------")
        print("----------------")
        print("[0   0]")
        print("[  0  ]")
        print("[0   0]")
    elif c == 6 and c==a:
        print("congratulations")
        print("----------------")
        print("----------------")
        print("[0 0 0]")
        print("[     ]")
        print("[0 0 0]")
    elif c>6:
     print("plz input a valid digit")
    else:
        print("congratulations you Lose")
    print("\n")
    x = input("press y to roll again and n to exit: ")
    print("\n")
