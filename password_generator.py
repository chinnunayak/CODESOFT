#Program For password generator
import random
import  string

#Main Program
def generate_password(length):
     characters = string.ascii_letters + string.digits + string.punctuation
     password = '' .join(random.choice(characters)for _ in range(length))
     return password

while True:
    #Generate User name
    username = input("Enter your username(or type 'q' to exit):")
    #Generate Quit Option for Exit Program
    if username.lower() == 'q':
          break
    #Prompt the user to specify the desired password length
    user_input = input(f"Enter the describe password length for {username}: ")
    try:
        length = int(user_input)
        if length > 0:
               #Generate the Password
               password = generate_password(length)
               #Display the Generate Password
               print(f"Generate Password for {username}:{password}")
        else:
               print("Print enter a positive length.")
               
    except ValueError:
          print("Invalid input. Please enter a valid integer length.")

#Display  Exit
print("GoodBye!!!!!!!!!!!!")