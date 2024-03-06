import json
import os

#writing data to json file
def write_to_File():
    user_data=[]
    while True:
        name=input("input name or 'quit' to quit the program:")
        if name=="quit":
            break
        email=input("Email please")
        contact=input("Contact: ")
        #creating a dictionary
        data={"Name":name, "email":email, "Contact":contact}
        user_data.append(data)
    if os.path.exists("jsonfile.json"):
        with open("jsonfile.json", "r") as file:
            existing_data=json.load(file)
        user_data.extend(existing_data)
    

    with open ("jsonfile.json", "w") as file:
        json.dump(user_data, file)
        
        print("Data written to file successfully!")

#Reading from json file
def search_file():
    if os.path.exists("jsonfile.json"):
        with open("jsonfile.json", "r") as file:
            new_data=json.load(file)
            name=input("Enter name to search")
            found=False
            for data in new_data:
                if data.get("Name")==name:
                    print(data)
                    found=True

    else:
        print("File does not exist")

def read_file():
    if os.path.exists("jsonfile.json"):
        with open("jsonfile.json", "r") as file:
            data=json.load(file)
        for mydata in data:
            print("Name: "+str(mydata.get("Name")))
            print("Email: "+str(mydata.get("email")))
            print("Contact: "+str(mydata.get("contact")))
            print("\n")
    else:
        print("file not found")
#Edit record method
def edit_file():
    if not os.path.exists("jsonfile.json"):
        print("file not found")
        return
    else:
        name=input("Enter name of record to edit: ")
        found=False
        with open("jsonfile.json", "r") as file:
            user_details=json.load(file)
            for user in user_details:
                if name==user.get("Name"):
                    new_name=input("Enter new name: ")
                    user["Name"]=new_name
                    found=True
            if not found:
                print("record not found")
            else:
                print(name+" updated successfully")
        with open("jsonfile.json","w") as file:
            json.dump(user_details, file)
#delete record method
def delete_record():
    if not os.path.exists("jsonfile.json"):
        print("file not found")
        return
    else:
        name=input("Enter name of record to delete: ")
        found=False
        with open("jsonfile.json", "r") as file:
            user_details=json.load(file)
            for user in user_details:
                if name==user.get("Name"):
                    user_details.remove(user)
                    found=True
            if not found:
                print("record not found")
            else:
                print("Record deleted successfully:")
        with open("jsonfile.json", "w") as file:
            json.dump(user_details, file)
            print("record successfully removed..")
#menu design           
while True:
    choice=input(f"1: to store a record in a file: \n 2: To Search a record in the file: \n 3: To Edit a record stored in a file: \n 4: To delete a record: \n 5: To read all the records in a file. \n 0 To exit the program ")
    if choice=="1":
        write_to_File()
    elif choice=="2":
        search_file()
    elif choice=="3":
        edit_file()
    elif choice=="4":
        delete_record()
    elif choice=="5":
        read_file()
    elif choice=="0":
        break
    else:
        print("Unknown selection")






