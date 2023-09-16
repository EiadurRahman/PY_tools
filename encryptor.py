import os
import datetime
from cryptography.fernet import Fernet as fcode
from tkinter import filedialog

key_path = r'config/secret_key.key'
dir_path = filedialog.askdirectory()
directory_content = os.listdir(dir_path)


if not os.path.exists(key_path):
    print('creating key file.....')
    key = fcode.generate_key()
    os.mkdir('config')
    with open(key_path,'wb') as secret_key:
        secret_key.write(key)
    print('done!')
    with open(key_path,'rb') as secret_key:
        key = secret_key.read()
elif os.path.exists(key_path) :
    print('working with already existing key')
    with open(key_path,'rb') as secret_key:
        key = secret_key.read()
for file in directory_content:
    file_path = os.path.join(dir_path,file)
    # print(file)
    if os.path.isfile(file_path) and not '.ur' in file:
        print(f'encripting : {file}')

        with open(file_path,'rb') as content:
            content = content.read()
            encrypted_data = fcode(key).encrypt(content)
            with open(file_path,'wb') as result:
                result.write(encrypted_data)
                print(f'done encrypting {file}')
       

        # file_name = os.path.basename(file_path)
        
        try :
            encrypt_file_name = fcode(key).encrypt(file.encode('utf_8'))
            print(f'renaming {file} to {encrypt_file_name}')
            os.rename(file_path,os.path.join(dir_path,encrypt_file_name.decode('utf-8')+'.ur'))
        except:
            print(f"encrypting file name isn't working for somereason \n just adding '.err' ext to it")
            os.rename(file_path,os.path.join(dir_path,f'{file}.err'))
        print('  ')
    elif '.ur' in file:
        print(f"{file} is already encrypted ")
print('''
      
            ENCRYPTION IS DONE.
                        

''')