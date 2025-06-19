import sys 
def main():
    param = sys.argv[1:]
    if len(param) < 2:
        print("none")
    else:
        for param in reversed(params):
         print(param)
if __name__ == "__main__":
    main()