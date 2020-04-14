from random import randint


class WebUser:
    def __init__(self, user_name, user_age, user_gender, user_location, user_email):
        self.name = user_name
        self.age = user_age
        self.gender = user_gender
        self.location = user_location
        self.email = user_email
        self.passkey = ""
        self.login_attempts = 0
        self.fee = 0

    def fee_payment(self):
        self.fee = eval(input("Pay $85.49 and proceed for restoration.."))
        if self.fee == 85.49:
            print("****PLEASE WAIT WHILE WE ARE RESTORING YOU ACCOUNT********\nAccount restored :")
            self.user_info_display()
        else:
            print("!!!!FIGURES UNMATCHED!!!!!...Try again..")
            self.fee_payment()

    def greet_user(self):
        print("\nHello Mr/Mrs.", self.name.upper())
        print("Thank you for registering on our web..")
        print("Your details are as follows : ")

    def passkey_generator(self):
        x = str(randint(1, 100)) + self.name[:3] + self.gender[:3] + self.location[:3]
        print("YOUR NEW PASSWORD : ", x)

    def user_info_display(self):
        print("User_Name : ", self.name)
        print("User_Age  : ", self.age)
        print("User_Gender : ", self.gender)
        print("User_Location : ", self.location)
        print("User_email_id : ", self.email)

    def check_passkey(self):
        while True:
            print("Enter your password [chance", self.login_attempts + 1, "] : ")
            pass_word = input()
            self.passkey = pass_word
            if self.passkey != "I_am_a_geek_360 ":
                self.login_attempts += 1
                if self.login_attempts > 2:
                    return False
            else:
                return True

    def reset_attempt(self):
        self.login_attempts = 0


user = WebUser("AB_HI_RAM", 18, "MALE", "Man_gal_ore", "ab_hi_bs360")
result = user.check_passkey()
while not result:
    print("INVALID ENTRY.....LOGIN UNSUCCESSFUL")
    choice = input("Forget Password??? [yes/no]")
    if choice == "yes":
        user.reset_attempt()
        result = user.check_passkey()
    else:
        print("--------\n1. Create new account\n2. Pay $85.49 for account restoration..")
        step = int(input())
        if step == 1:
            new_name = input("Name : ")
            new_age = input("Age : ")
            new_gender = input("Gender : ")
            new_location = input("Location : ")
            new_email = input("Email : ")
            print("*****YOUR NEW ACCOUNT IS BEING PROGRAMMED*****")
            new_user = WebUser(new_name, new_age, new_gender, new_location, new_email)
            new_user.greet_user()
            new_user.user_info_display()
            new_user.passkey_generator()
            break
        elif step == 2:
            verify = input("Enter your user_name/name for verification..")
            if verify == "AB_HI_RAM":
                user.fee_payment()
            else:
                print("***INVALID USERNAME>>>> PORTAL TERMINATED FOR SECURITY REASONS***")
            break
if result:
    print("\nLogin success_full------------------------------------------")
    user.user_info_display()
