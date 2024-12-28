import subprocess
import requests
import re

from tqdm import tqdm
from time import sleep
from bs4 import BeautifulSoup

my_file = open("CHIRBASE_SEPARATION_UPDATED.txt", "r")
link_file = open("CHIRBASE_SEPARATION_LINKS.txt", "a")
out_file = open("CHIRBASE_SEPARATION_DIRECTION.txt", "a")

lines = my_file.readlines()

for smile in tqdm(lines):
    smile = smile.split("\n")[0]
    print(smile)

    # Get redirect url
    url = str(subprocess.check_output('curl -w "%{url_effective}\n" -I -L -s -S -g "https://www.chemspider.com/Search.aspx?q=' + smile + '" -o /dev/null', shell=True)).split("b'")[1].split("'")[0]

    # Get direction of redirect
    if "Chemical-Structure" in url:
        reqs = requests.get(url)
        soup = BeautifulSoup(reqs.text, 'html.parser')

        # Check for titles as well as synonyms
        big_soup = soup.find_all("title") + soup.find_all("div", class_="syn")

        for name in big_soup:
            name = str(name)
            # Check for optical direction
            if re.search(".*\(\+\).*", name):
                out_file.write(str([smile, url, "+"]) + "\n")
                print("(+)")
                break
            elif re.search(".*\(\-\).*", name):
                out_file.write(str([smile, url, "-"]) + "\n")
                print("(-)")
                break
            else:
                print("nada")
                continue

            link_file.write(str(url) + "\n")
    else:
        link_file.write("NO REDIRECT")
        
        
    sleep(1)

my_file.close()
link_file.close()
out_file.close()
