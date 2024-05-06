import argparse #its a command line tool and we use it because it consume fewer system resources as compared to GUI
import string   #string import isliye kraya gya h kyunki password m ascii_letters/digit/punctuation use hoske. Built in function ke sath aise koi module nhi hote string     
import secrets  #secret use isliye kra h kyunki password random or secure kra jaske
a=int(input('How Long You Wish To Set Your Password?'))
def generate_password(length):#used to give a parameter
    """Generate a random password."""
    alphabet = string.ascii_letters + string.digits + string.punctuation#combination ie ascii letters + digits +specialchar
    password = ''.join(secrets.choice(alphabet) for _ in range(length))# this is used to pick random password . It is similar to random library
    return password# here we returned the value and store

def main():
    parser = argparse.ArgumentParser(description="Generate a random password")#used to link the command line tool for generation of password
    parser.add_argument("-l", "--length", type=int, default=a, dest="length")#this step is basically used for default value ie 12 and -l is aliasing and --self is used to start the char character with the int and other forms
    args = parser.parse_args()#here the value of 12 length is stored

    if args.length <= 0:#this condition will never be true as default value is 12 but incase the user use non ositive number then it will show an error
        print("Error: Length should be a positive integer.")
        return

    password = generate_password(args.length)# the return function stored here and then will print in next step
    print("Generated Password:", password)

if __name__ == "__main__":
    main()# this is used to call the function otherwise the output will not be showed
