from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import MolChiral
from tqdm import tqdm
import ast
import copy

#bigarr = open("standard_smiles.txt", "r").readlines()
bigarr = open("oldata.txt", "r").readlines()
hugearr = open("oldata.txt", "r").readlines()
out = open("full2.txt", "a")
outarr = []

for i, x in enumerate(hugearr):
    hugearr[i] = ast.literal_eval(x)

# print(list(hugearr[131].values())[0])

#sarr = copy.deepcopy(bigarr)
for i, x in enumerate(bigarr):
    bigarr[i] = list(ast.literal_eval(x).keys())[0]

for i, smile in tqdm(enumerate(bigarr), total=25273):
    #print(smile)
    ps = Chem.SmilesParserParams()
    ps.removeHs = False
    m1 = Chem.MolFromSmiles(smile, ps)
    m1 = Chem.AddHs(m1)

    try:
        if MolChiral.IsMolChiral(m1):
            sign = list(hugearr[i].values())[0]
            outarr.append([smile, sign])
            AllChem.EmbedMolecule(m1)
            em1 = MolChiral.GetEnantiomer(m1, forceHs=True)
            tmp = Chem.MolToSmiles(em1, isomericSmiles=True)
            if sign == "(+)":
                outarr.append([str(tmp), "(-)"])
            elif sign == "(-)":
                outarr.append([str(tmp), "(+)"])
            else:
                outarr.remove([m1, bigarr[i][1]])
        else:
            continue
    except:
        print("bruh what")

checkarr = []
for x in outarr:
    if x[0] in checkarr:
        continue
    else:
        checkarr.append(x)

for y in checkarr:
    out.write(f"{y}\n")

