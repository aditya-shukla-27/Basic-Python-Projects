
your_email = input("Please enter your emailid\n").split("@")
user_name = your_email[0]
domain_name = your_email[1]
print(f"The username is {user_name} and domain name is {domain_name}")



'''
Alternate Code for this program

email = input("Enter Your Email: ").strip()
username = email[:email.index("@")]
domain_name = email[email.index("@")+1:]
format_ = (f"Your user name is '{username}' and your domain is '{domain_name}'")
print(format_)'''