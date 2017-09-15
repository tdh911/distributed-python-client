from random import choice
from string import digits, ascii_uppercase

def main():
    print "".join(choice(digits + ascii_uppercase) for i in range(16))    

if __name__ == "__main__":
    main()
