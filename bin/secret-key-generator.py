from random import choice, randint
from string import digits, ascii_uppercase, ascii_lowercase

def main():
    length = randint(15, 25)
    print "".join(choice(digits + ascii_uppercase + ascii_lowercase) for i in range(length))    

if __name__ == "__main__":
    main()
