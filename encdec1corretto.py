from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization

import base64

with open('private_key.pem', 'rb') as key_file:
    
    private_key = serialization.load_pem_private_key(key_file.read(),password=None) 
    password='mypassword'

with open('pubblic_key.pem', 'rb') as key_file:
    pubblic_key = serialization.load_pem_public_key(key_file.read())

message = 'ciao, epicode spacca'

encrypted = pubblic_key.encrypt(message.encode(), padding.PKCS1v15())
decrypted = private_key.decrypt(encrypted, padding.PKCS1v15())



print("messaggio criptato: ", base64.b64encode(encrypted).decode('utf-8'))
a = input("password necessaria: ")
if a == password:
    print("messaggio decriptato: ", decrypted.decode('utf-8'))
else:
    print("accesso negato")