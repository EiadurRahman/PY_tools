import os
from cryptography.fernet import Fernet as fcode
from tkinter import filedialog

key_path = r'config/secret_key.key'
if os.path.exists(key_path) :
        
    dir_path = filedialog.askdirectory()
    directory_content = os.listdir(dir_path)
    print('working with already existing key')
    with open(key_path,'rb') as secret_key:
        key = secret_key.read()
    for file in directory_content:
        file_path = os.path.join(dir_path,file)
        # print(file)
        if os.path.isfile(file_path) and '.ur' in file or '.err' in file:
            print(f'decrypting : {file}')
        
            with open(file_path,'rb') as content:
                content = content.read()
                decrypted_data = fcode(key).decrypt(content)
                with open(file_path,'wb') as result:
                    result.write(decrypted_data)
                    print(f'done decrypting {file}')

            ext = file[:-len('.ur')]
            err_ext = file[:-len('.err')]
            
            # print(f'renaming {file} to {ext}')
            if '.ur' in file:
                print(f'renaming {file} to orginal......')
                file_name = os.path.basename(file_path)
                decript_file_name = fcode(key).decrypt(ext.encode('utf-8'))
                os.rename(file_path,os.path.join(dir_path,decript_file_name.decode('utf-8')))
                print(f'decrypted file name {decript_file_name}')
                print(' ')
            elif '.err' in file:
                print("dealing with '.err' files")
                err_ext = file[:-len('.err')]
                os.rename(file_path,os.path.join(dir_path,err_ext))
                print(f'decrypted file name {file}')
                print(' ')
      
        else:
            print(f"{file} isn't encrypted")
else:
    print('KEY file not found')

print('''

      
            DECRYPTION IS DONE.
                        

''')