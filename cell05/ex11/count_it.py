import sys

def main ():
    params = sys.argv[1:]
    if len(params) == 0:
       print("none")
    else: 
        print(f"parameters : {len(param)}")
        for p in param:
            print(f"{p}; {len(p)}")

if __name__  ==  "__main__":
   main()

