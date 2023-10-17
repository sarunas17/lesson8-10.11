# Create a program witch takes 5 different (minmum)  variables containing strings for username and password.
# The string should look like : "username='', password=''; username='',password='';....etc"
# Start Endless loop allowing to enter username and password and 
# check ff credentials are correct stop endless loop and print greeting message, otherwise print 'wrong credentials' and ask to enter password and username again. 
# The program should show numbers of times you tried to enter both credentials.

# For storing account information use dict , all data should be lowercase. and extra symbols (@, %, $ etc and numbers). 
# If in password numbers or symbols are not provided, the program should add additional value to dictionary as a value, names 'improved password'

input_splited = []
while len(input_splited) < 20:
 user_input = input("Enter minimum 5 usernames and passwords in the format username='' , password=''; : ")
 input_replaced = user_input.replace(" ","").replace("'","").replace(";",",").replace("=",",")
 input_splited = input_replaced.split(",")

list = []
list = input_splited[1::2]
list_username = list[::2]
list_password = list[1::2]
user_data = dict(zip(list_username, list_password))



attempts = 1

while True:
   username_input = input("Enter your username: ")
   password_input = input("Enter your password: ")
   for username, password in user_data.items():
        if username == username_input and password == password_input:
          print("Welcome")
          break
   else: 
          print(f"Incorrect username or password. Please try again. Number of attempts: {attempts}")
          attempts = attempts + 1
          continue
   break
          

# has_numbers = any(char.isdigit() for char in password)
# has_symbols = any(char in "!@#$%^&*()-_+=<>?[]{}" for char in password)

# if not has_numbers or not has_symbols:
#     if not has_numbers:
#         password += '123'  
#     if not has_symbols:
#         password += '!@#'  

# print("Improved Password:", password)

                  

                  
