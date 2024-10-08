# TODO: This application should be modified to work for all ages and provide customized responses.

def main():
    name = str(input("Enter your name: "))
    age = int(input("Enter your age: "))

    if age < 0:
        print("Error: Age cannot be negative.")
        return  # Exit the program if age is invalid.

    if age < 18:
        print("Sorry, you are not eligible to order a laptop.")
    
    print(f"Welcome to the love system! This is a system created by Niranajan, nice to meet you, {name}!")

    girl_name = str(input("Enter your lover's name: "))
    if girl_name == "":
        print("Sorry, you need to enter your lover's name.")
    else:
        print(f"Congratulations on your wedding anniversary, {girl_name}!")

    love = str(input("Are you in love with me (y/n)? "))
    if love.lower() == "y":
        print("I'm glad you are in love with me!")
        single = str(input("Are you single (y/n)? "))
        if single.lower() == "y":
            print("I'm sorry, you are single. :(")
        else:
            print("That's great! You're not single! :)")
    else:
        print("I'm sorry, you are not in love with me. :(")

    # Call the function for boyfriend's name
    boy_name = love_boyfriend()

    # Call the function to display information, including age
    your_information(name, girl_name, boy_name, age)

def love_boyfriend():
    boy_name = str(input("Enter your boyfriend's name: "))
    if boy_name == "":
        print("Sorry, you need to enter your boyfriend's name.")
        return None  # Return None if no boyfriend's name is provided
    else:
        print(f"Congratulations on your wedding anniversary, {boy_name}!")
    return boy_name  # Return the boyfriend's name

def your_information(name, girl_name, boy_name, age):
    print("\nThis is the information you provided:")
    print(f"Your name is {name}.")
    print(f"Your lover's name is {girl_name}.")
    print(f"Your boyfriend's name is {boy_name if boy_name else 'not provided'}.")
    
    see_info = str(input("Do you want to see your information again? (y/n) "))
    if see_info.lower() == "y":
        print(f"\nHere is your information:\nName: {name}\nAge: {age}\nLover's Name: {girl_name}\nBoyfriend's Name: {boy_name if boy_name else 'not provided'}")

# Start the program
main()
