import os
import json
from urllib import response
import requests # pip install req
from bs4 import BeautifulSoup  #pip install bs4 - its parses html

Google_Image = \
    'https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&'
Save_Folder = 'images'
usr_agent = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,/;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive',
}

def main():
    if not os.path.exists(Save_Folder):
        os.mkdir(Save_Folder)
    download_images()

def download_images():
    data = input("what are you looking for?")                         
    nimages = int(input("How many images do you want?"))                                                     

    print('start searching...')

    searchurl = Google_Image + 'q+' + data
    print(searchurl)
    
    response = requests.get(searchurl, headers=usr_agent)
    html = response.text
    soup = BeautifulSoup('html.parser')
    results = soup.findAll('div',{'class':'rg_meta'}, limit= nimages)

    imagelinks = []
    for result in results:
        text = result.text
        print(text)
        text_dict = json.loads(text)
        link = text_dict['ou']
        imagelinks.append(link)
    print(f'found {len(imagelinks)} images')

    print('start dopwnloading.....')

    for i , imagelink in enumerate(imagelinks):
        response = requests.get(imagelink)

        imagename = Save_Folder + '/' + data + str(i+1) + '.jpg'
        with open(imagename, 'wb') as file:
            file.write(response.content)

    print('done')

if __name__ =='__main__':
    main()