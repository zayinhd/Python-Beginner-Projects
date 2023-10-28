""" Slice an email address : Eg. example123@email.com should Output example123, email, com. """

# Slice Function
def sliced(email):
    # destructuring email values
    (username, domain) = email.split("@")
    # destructuring domain values
    (domain, extension) = domain.split(".")

    print("The Username is : ",username)
    print("The Domain is : ",domain)
    print("The Extension is : ",extension)


while(True):
    print("================================================")
    print("Email Slicer")
    print("================================================")

    email_address = input("Please enter the email address : ")
    sliced(email_address)
    