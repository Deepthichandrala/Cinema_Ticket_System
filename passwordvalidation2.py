
import maskpass
users={'deep':'deep123','hari':'hari234','jabi':'jabi123'}
def login():
    attempts=0
    username=input("username:")
    if username in users:
        valid_username=True
    else:
        print("Account Does't exit!")
        return   
    
    while attempts<=3:
        password=maskpass.advpass("password:")
        if password==users[username]:
            print("login succesful!.")
            break
            
        elif attempts<3:       
            print("wrong password!,Try again")
            attempts+=1                        
        else :
                print("Account blocked!") 
                break              
login()            
        
            