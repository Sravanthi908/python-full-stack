#function
#function
def add_contact(contacts):
    file =open("./file.txt","a")
    name = input("Enter Contact Name :")
    mobile = int(input("Enter mobile number :"))
    contacts[name] = mobile
    file.write(f"{name} : {mobile}\n")
    file.close()

def view_contacts(contacts):
    print("\n")
    for i in contacts:
        print(f"{i} : {contacts[i]}")

def delete_contact(contacts):
    name_to_delete = input("Enter contact name to delete :")
    del contacts[name_to_delete]
    print("deleted contact " , name_to_delete)

def find_contact(contacts):
    query = input("Enter name to search : ")
    found = False
    for key in contacts:
        if query in key:
            print(f"{key} => {contacts[key]}")
            found = True
    if not found:
        print("name not Found!!!")

def edit_contact(contacts):
    name_to_edit = input("Enter contact name to edit :")
    number = int(input("Enter new number: "))
    contacts[name_to_edit] = number
    file=open("./file.txt","r")
    data=file.read()
    list_data=data.split(" ")
    mobile_dict={}
    for name in list_data:
        splitted_item=name.split("")
        mobile_dict(name[0]==int(mobile[1]))
        print(mobile_dict)

    file.close()
    
