# Create a program witch takes 5 different (minmum)  variables containing strings for username and password.
# The string should look like : "username='', password=''; username='',password='';....etc"
# Start Endless loop allowing to enter username and password and 
# check ff credentials are correct stop endless loop and print greeting message, otherwise print 'wrong credentials' and ask to enter password and username again. 
# The program should show numbers of times you tried to enter both credentials.

# For storing account information use dict , all data should be lowercase. and extra symbols (@, %, $ etc and numbers). 
# If in password numbers or symbols are not provided, the program should add additional value to dictionary as a value, names 'improved password'

input_splited = []
while len(input_splited) < 10:
 user_input = input("Enter minimum 5 usernames and passwords in the format username= , password= ; : ")
 input_replaced = user_input.replace(";", ",").replace(" ","")
 input_splited = input_replaced.split(",")

list= []
for value in input_splited:
    list.append(value[9:])
    list_username = list[::2]
    list_password = list[1::2]

attempts = 1

while True:
    
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in list_username and password in list_password:
        print("Welcome")
        break
    else: 
        print(f"Incorrect username or password. Please try again. Number of attempts: {attempts}")
        attempts = attempts + 1

                  
