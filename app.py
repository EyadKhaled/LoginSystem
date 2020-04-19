# Users List
users = []


# Login Function
def login():
    email = input("> Your Email:\n")
    password = input("> Your Password:\n")

    try:
        if users[users.index({"email": email, "password": password})]:
            name = email[:email.index("@")]
            host = email[email.index("@") + 1:]

            print("> Successfully Logging In !\n")
            print("#" * 40)
            print(f" Welcome Back {name} ".center(40, "#"))
            print(f" Your Host {host} is Good! ".center(40, "#"))
            print("#" * 40)
    except ValueError:
        print("\n> Wrong Email or Password.")
        loginSystem()


# Signup Function
def sign():
    email = input("> Your Email:\n")
    password = input("> Your Password\n")

    users.append({"email": email,
                  "password": password})

    print("> Successfully Signup !")
    loginSystem()


# Startup Function
def loginSystem():
    # Login Or Signup ?
    option = input("> Do you want to login(l) or signup(s)?\n").strip().lower()

    # Check
    if option == "login" or option == "l":
        login()

    elif option == "signup" or option == "s":
        sign()

    else:
        print("> You Must Type \"Login\" or \"Signup\"")
        loginSystem()


loginSystem()
