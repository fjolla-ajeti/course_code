#Task3
#The name check.
#Write a program that has a variable with your name stored (in lowercase) and then asks for your name as input. 
#The program should check if your input is equal to the stored name even if the given name has another case, e.g., if your input is “Anton” and the stored name is “anton”, it should return True.
stored_name = "fjolla"
user_input = input("Enter your name: ")

if user_input.lower() == stored_name:
    print("True")
else:
    print("False")
