email = input()
if "@" in email:
    email_lst = email.split("@")
    left_name = email_lst[0]
    if email_lst[0] == "":
        print("Invalid email")
    elif len(email_lst[0]) >3:
        stars = "*"*(len(email_lst[0])-3)
        print(f"{left_name[:3]}{stars}@{email_lst[1]}")
    else:
        print(email)
else:
    print("Invalid email")