import sys 
if len(sys.argv) ==2:
    paramether = sys.argv[1]
    user_input = input("what was the parameter? ")

    if user_input == paramether:
        print("Good job!")
    else:
          print("Nope, sorry...")
else:
        print("none")    