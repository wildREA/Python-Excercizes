# --------- DATA LIBRARY ---------
nullChars1 = ["/", "\\", "=", "+", "?", "´", "¨", "*", "^", "`", "!", "#", "¤", "%", "&", ";", ":"]
nullChars2 = ["(", ")", "\"", "[", "]", "{", "}", "|", "§", "½", "€", "£", "$", "€", "<", ">", ","]
invalidCharacters = nullChars1 + nullChars2

# --------- CODE ---------
while True:
    email = input("Email: ")[:30]  # no more than 30 characters
    if len(email) >= 7 <= 30:
        if email not in invalidCharacters:
            if email.count("@"):
                if email.count("gmail") or email.count("yahoo"):
                    if email.endswith(".dk") or email.endswith(".com"):
                        print("Valid email address.")
                        break
                    else:
                        print("Error: Email address must end with \".com\" or \".dk\".")
                else:
                    print("Error: Email address must contain a valid domain.")
            else:
                print("Error: Email address must contain \"@\".")
        else:
            print("Error: No illegal characters.")
    else:
        print("Error: Email address must be within a range of 7-30 character limit.")
