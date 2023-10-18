# Create a program witch takes 5 different (minmum)  variables containing strings for username and password.
# The string should look like : "username='', password=''; username='',password='';....etc"
# Start Endless loop allowing to enter username and password and 
# check ff credentials are correct stop endless loop and print greeting message, otherwise print 'wrong credentials' and ask to enter password and username again. 
# The program should show numbers of times you tried to enter both credentials.

# For storing account information use dict , all data should be lowercase. and extra symbols (@, %, $ etc and numbers). 
# If in password numbers or symbols are not provided, the program should add additional value to dictionary as a value, names 'improved password'

input_splited = []
while len(input_splited) < 5:
 user_input = input("Enter minimum 5 usernames and passwords in the format username='' , password=''; : ")
 input_replaced = user_input.replace(" ","").replace("'",'"').replace("=",": ").replace(",", ", ").replace("username", '"username"').replace("password", '"password"')
 input_splited = input_replaced.split(";")


user_data = []
for item in input_splited:
    user_data_dict = {}
    for key_value_pair in item.split(', '):
        key, value = key_value_pair.split(': ')
        user_data_dict[key.strip('"')] = value.strip('"')
    user_data.append(user_data_dict)

attempts = 1

while True:
   username_input = input("Enter your username: ")
   password_input = input("Enter your password: ")
   for user_info in user_data:
        if user_info['username'] == username_input and user_info['password'] == password_input:
          print("Welcome")
          break
   else: 
          print(f"Incorrect username or password. Please try again. Number of attempts: {attempts}")
          attempts = attempts + 1
          continue
   break
          

for char in password_input:
     has_symbols = any(char in "!@#$%^&*()-_+=<>?[]{}1234567890" for char in password_input)
     if not has_symbols:
          improved_password = password_input + "=/+@753"
          index_to_update = None
          for index, user_dict in enumerate(user_data):
            if user_dict.get('password') == password_input:
                index_to_update = index
            if index_to_update is not None: 
                user_data[index_to_update]['Improved_password'] = improved_password
           
print(user_data)

