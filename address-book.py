#!/usr/bin/python
#filename address-book.py
import pickle
import os
class Contact:
    def __init__(self,name,email,phone):
        self.name=name
        self.email=email
        self.phone=phone
        
    def __str__(self):
        return "Name:{0}\nEmail address:{1}\nPhone:{2}".format(self.name,self.email,self.phone)
        
    def change_name(self,name):
        self.name=name
        
    def change_email(self,email):
        self.email=email
        
    def change_phone(self,phone):
        self.phone=phone
        
def add_contact():
    address_book_file=open("address_book_file","r")
    is_file_empty=os.path.getsize("address_book_file")==0
    if not is_file_empty:
        list_contacts=pickle.load(address_book_file)
    else:
        list_contacts=[]
    try:
        contact=get_contact_info_from_user()
        address_book_file=open("address_book_file","w")
        list_contacts.append(contact)
        pickle.dump(list_contacts,address_book_file)
        print "Contact added"
    except KeyboardInterrupt:
        print "Contact not added"
    except EOFError:
        print "Contact not added"
    finally:
        address_book_file.close()
    
def get_contact_info_from_user():
    try:
        contact_name=input("Enter contact name\n")
        contact_email=input("Enter contact email\n")
        contact_phone=input("Enter contact phone number\n")
        contact=Contact(contact_name,contact_email,contact_phone)
        return contact
    except EOFError as e:
        #print "You entered end of file. Contact not added"
        raise e
    except KeyboardInterrupt as e:
        #print "Keyboard interrupt. Contact not added"
        raise e
    
def display_contacts():
    address_book_file=open("address_book_file","r")
    is_file_empty=os.path.getsize("address_book_file")==0
    if not is_file_empty:
        list_contacts=pickle.load(address_book_file)
        for each_contact in list_contacts:
            print each_contact
    else:
        print "No contacts in address book"
        return
    address_book_file.close()
    
def search_contact():
    #search_name=input("Enter the name\n")
    address_book_file=open("address_book_file","r")
    is_file_empty=os.path.getsize("address_book_file")==0
    if not is_file_empty:
        search_name=input("Enter the name\n")
        is_contact_found=False
        list_contacts=pickle.load(address_book_file)
        for each_contact in list_contacts:
            contact_name=each_contact.name
            search_name=search_name.lower()
            contact_name=contact_name.lower()
            if(contact_name==search_name):
                print each_contact
                is_contact_found=True
                break
        if not is_contact_found:
            print "No contact found with the provided search name"
    else:
        print "Address book empty. No contact to search"
    address_book_file.close()

def delete_contact():
    #name=input("Enter the name to be deleted\n")
    address_book_file=open("address_book_file","r")
    is_file_empty=os.path.getsize("address_book_file")==0
    if not is_file_empty:
        name=input("Enter the name to be deleted\n")
        list_contacts=pickle.load(address_book_file)
        is_contact_deleted=False
        for i in range(0,len(list_contacts)):
            each_contact=list_contacts[i]
            if each_contact.name==name:
                del list_contacts[i]
                is_contact_deleted=True
                print "Contact deleted"
                address_book_file=open("address_book_file","w")
                if(len(list_contacts)==0):
                    address_book_file.write("")
                else:
                    pickle.dump(list_contacts,address_book_file)
                break
        if not is_contact_deleted:
            print "No contact with this name found"
            
    else:
        print "Address book empty. No contact to delete"
    address_book_file.close()
    
def modify_contact():
    address_book_file=open("address_book_file","r")
    is_file_empty=os.path.getsize("address_book_file")==0
    if not is_file_empty:
        name=input("Enter the name of the contact to be modified\n")
        list_contacts=pickle.load(address_book_file)
        is_contact_modified=False
        for each_contact in list_contacts:
            if each_contact.name==name:
                do_modification(each_contact)
                address_book_file=open("address_book_file","w")
                pickle.dump(list_contacts,address_book_file)
                is_contact_modified=True
                print "Contact modified"
                break
        if not is_contact_modified:
            print "No contact with this name found"
    else:
        print "Address book empty. No contact to delete"
    address_book_file.close()
    
def do_modification(contact):
    try:
        while True:
            print ("Enter 1 to modify email and 2 to modify address and 3 to quit without modifying")
            choice=input()
            if(choice=="1"):
                new_email=input("Enter new email address\n")
                contact.change_email(new_email)
                break
            elif(choice=="2"):
                new_phone=input("Enter new phone number\n")
                contact.change_phone(new_phone)
                break
            else:
                print "Incorrect choice"
                break
    except EOFError:
        print "EOF Error occurred"
    except KeyboardInterrupt:
        print "KeyboardInterrupt occurred"
    
print "Enter 'a' to add a contact, 'b' to browse through contacts, 'd' to delete a contact, 'm' to modify a contact, 's' to search for contact and 'q' to quit"
while True:
    choice=input("Enter your choice\n")
    if choice == 'q':
        break
    elif(choice=='a'):
        add_contact()
    elif(choice=='b'):
        display_contacts()
    elif(choice=='d'):
        delete_contact()
    elif(choice=='m'):
        modify_contact()
    elif(choice=='s'):
        search_contact()
    else:
        print "Incorrect choice. Need to enter the choice again"
        

