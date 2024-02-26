import os
def sign_in():
  username = input("Enter username: ")
  password = input("Enter password: ")

  with open("C:/Users/94772/Downloads/user.txt", 'r') as file:
   # Read lines from the file and strip newline characters
   valid_credentials = [line.strip() for line in file.readlines()]

  print("Valid Credentials:", valid_credentials)  # Add this line for debugging

  # Check if there are exactly two values in the list
  if len(valid_credentials) == 2:
   valid_username, valid_password = valid_credentials
   if username == valid_username and password == valid_password:
    print("Welcome to the Library Management System!")
    return True
   else:
    print("Invalid username or password. Please try again.")
    return False
  else:
   print("Invalid file format. Please check the authentication file.")
   return False


if __name__ == "__main__":
 #authendicate =
 sign_in()

#while authendicate:


