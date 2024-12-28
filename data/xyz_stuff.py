from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.Chem import AllChem
from tqdm import tqdm


inchi = "InChI=1S/C42H69Cl3O7/c1-3-5-7-9-11-13-15-17-19-21-23-25-27-29-31-33-39(46)49-35-38(36-50-41(48)51-37-42(43,44)45)52-40(47)34-32-30-28-26-24-22-20-18-16-14-12-10-8-6-4-2/h11-14,17-20,38H,3-10,15-16,21-37H2,1-2H3/b13-11-,14-12-,19-17-,20-18-/t38-/m1/s1"
inchi = "InChI=1S/C42H69Cl3O7/c1-3-5-7-9-11-13-15-17-19-21-23-25-27-29-31-33-39(46)49-35-38(36-50-41(48)51-37-42(43,44)45)52-40(47)34-32-30-28-26-24-22-20-18-16-14-12-10-8-6-4-2/h11-14,17-20,38H,3-10,15-16,21-37H2,1-2H3/b13-11-,14-12-,19-17-,20-18-/t38-/m1/s1"
inchi = "InChI=1S/C35H74NO5P/c1-5-7-9-11-13-15-17-19-21-23-25-27-30-39-33-35(34-41-42(37,38)32-29-36(3)4)40-31-28-26-24-22-20-18-16-14-12-10-8-6-2/h35H,5-34H2,1-4H3,(H,37,38)/t35-/m1/s1"

m = Chem.inchi.MolFromInchi(inchi)
m = Chem.AddHs(m)
AllChem.EmbedMolecule(m)
AllChem.EmbedMolecule(m)
AllChem.EmbedMolecule(m)
AllChem.EmbedMolecule(m)
AllChem.EmbedMolecule(m)
AllChem.EmbedMolecule(m)

_file = open(f"out.xyz", "a")
_file.write(Chem.MolToXYZBlock(m))
_file.close()

