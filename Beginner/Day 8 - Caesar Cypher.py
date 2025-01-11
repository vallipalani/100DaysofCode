import string

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
                                                          
                          88                                 
           ""             88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)

def encrypt():
    encoded_message = ""
    alphabetlist = list(string.ascii_lowercase + string.ascii_lowercase)
    for i in message:
        if i in alphabetlist:
            x = alphabetlist.index(i) + shift_number
            encoded_message = encoded_message + alphabetlist[x]
        else:
            encoded_message = encoded_message + i
    print("Here's the encoded result:", encoded_message)
    
def decrypt(): 
    decoded_message = ""
    alphabetlist = list(string.ascii_lowercase)
    for i in message:
            if i in alphabetlist:
                    x = alphabetlist.index(i) - shift_number
                    x = x%len(alphabetlist)
                    decoded_message = decoded_message + alphabetlist[x]
            else:
                decoded_message = decoded_message + i
    print("Here's the decoded result:", decoded_message)

x=True

while x==True:

    message = input("Type your message:\n").lower()
    shift_number = int(input("Type the shift number:\n"))
    encode_or_decrypt = input("Type 'encode' to encrypt, and type 'decode' to decrypt:\n").lower()

    message = list(message)
    
    if encode_or_decrypt == "encode":
        encrypt()
    else:
        decrypt()

    x=input("Do you want to go again? Type 'yes' or 'no'\n").lower()
    if x=="yes":
        x=True
    else:
        x=False
        print("Thank You!")
    
