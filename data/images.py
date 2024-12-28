from rdkit import Chem
from rdkit.Chem import Draw
from tqdm import tqdm
import ast


sarr = list(open("ilovedata.txt", "r").readlines())
for i, x in enumerate(sarr):
    sarr[i] = list(ast.literal_eval(x).keys())[0]

for i, smile in tqdm(enumerate(sarr)):
    mol = Chem.MolFromSmiles(smile)

    Draw.MolToFile(mol, "images/" + str(i + 1) + ".png")
