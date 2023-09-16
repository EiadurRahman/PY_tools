import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin,urlparse

while True:
    try:
        web_url = input('example : "https://example.com" (type "quit" or "q" ) > ')
        if web_url == 'quit' or web_url == 'q':
            break
        parsed_url = urlparse(web_url)
        web_name = parsed_url.netloc
        if 'www.' in web_name:
            web_name = web_name[4:]
        output_directory = f"scrap_download\{web_name}"
        os.makedirs(output_directory, exist_ok=True)



        res = requests.get(web_url)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, "html.parser")

            img_tags = soup.find_all("img")
            for img_tag in img_tags:
                img_url = img_tag.get('src')
                if img_url :
                    img_url = urljoin(web_url,img_url)
                    img_res = requests.get(img_url,stream=True)

                    if img_res.status_code == 200:
                        img_file_name = os.path.join(output_directory,os.path.basename(img_url))
                        if '.jpg' in img_file_name or '.png' in img_file_name:
                        # if True :
                            try:
                                with open(img_file_name, 'wb') as img_file:
                                    img_file.write(img_res.content)
                                print(f"Dwonloaded : {img_file_name}")
                            except:
                                print(f"Something is wrong with {img_file_name}")
                        else:
                            print(f"{img_file_name} isn't a '.jpg' or '.png' file")
                            
                    else:
                        print(f"COULDEN'T Dwonloaded : {img_file_name}")

                else:
                    print('PROBLAME WITH IMG_URL : ',img_url)
        else:
            print(f'Failed to fetch webpage: {web_url}')
    except:
        print("something isn't wrong....")
