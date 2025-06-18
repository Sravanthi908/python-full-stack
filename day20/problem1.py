def mails(mail):
    if '@'in mail and '.' in mail:
        return True
    else:
        return False
email =input( )
email=email[1:len(email)-1]
print(mails(email))




