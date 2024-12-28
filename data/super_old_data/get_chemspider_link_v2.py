import subprocess
import requests
import re
import os

from tqdm import tqdm
from time import sleep
from bs4 import BeautifulSoup

f1 = open("CHIRAL_SMILES_1.txt", "r")
f2 = open("CHIRAL_SMILES_2.txt", "r")
out_file = open("FINAL_DATA.txt", "a")
l1 = f1.readlines()
l2 = f2.readlines()

def get_opposite_direction(m):
    if m == "(+)":
        return "(-)"
    else:
        return "(+)"

def get_optical_direction(smile):
    # Get redirect url
    sleep(0.5)
    smile = smile.split("\n")[0]
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
                return "(+)"
            elif re.search(".*\(\-\).*", name):
                return "(-)"
            else:
                continue

    return None

for i in tqdm(range(6100, len(l1))):
    if (direction := get_optical_direction(l1[i])) is not None:
        out_file.write(str([l1[i], direction]) + "\n")
        out_file.write(str([l2[i], get_opposite_direction(direction)]) + "\n")
        out_file.flush()
        continue
    elif (direction := get_optical_direction(l2[i])) is not None:
        out_file.write(str([l1[i], get_opposite_direction(direction)]) + "\n")
        out_file.write(str([l2[i], direction]) + "\n")
        out_file.flush()
        continue
    else:
        continue



f1.close()
f2.close()
out_file.close()
