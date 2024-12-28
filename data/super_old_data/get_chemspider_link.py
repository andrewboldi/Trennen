import subprocess
import requests
import re
import os

from tqdm import tqdm
from time import sleep
from bs4 import BeautifulSoup

out_file = open("CHIRAL_SMILES.txt", "a")

for file_ in tqdm(os.listdir("files")):
    """
    my_file = open(file_, "r+")
    lines = my_file.readlines()
    smile = lines[len(lines) - 1].split("\t")[1].split("\n")[0]

    print(smile)
    """

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
                my_file.write(str([smile, url, "+"]) + "\n")
                out_file.write(str([smile, url, "+"]) + "\n")
                print("(+)")
                break
            elif re.search(".*\(\-\).*", name):
                my_file.write(str([smile, url, "-"]) + "\n")
                out_file.write(str([smile, url, "-"]) + "\n")
                print("(-)")
                break
            else:
                print("nada")
                continue
        
    my_file.close()
    sleep(1)

out_file.close()
