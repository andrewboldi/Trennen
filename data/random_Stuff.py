import logging
import sys
import os
import rdkit
from rdkit import rdBase, Chem
from rdkit.Chem import AllChem

# redirect logs to Python logger
rdBase.LogToPythonLogger()

class CaptureLogger(logging.Handler):
    """Helper class that captures Python logger output"""

    def __init__(self, module=None):
        super(CaptureLogger, self).__init__(level=logging.DEBUG)
        self.logs = {}
        self.devnull = open(os.devnull, 'w')
        rdkit.log_handler.setStream(self.devnull)
        rdkit.logger.addHandler(self)

    def __enter__(self):
        return self.logs

    def __exit__(self, *args):
        self.release()

    def handle(self, record):
        key = record.levelname
        val = self.format(record)
        self.logs[key] = self.logs.get(key, "") + val
        return False

    def release(self):
        rdkit.log_handler.setStream(sys.stderr)
        rdkit.logger.removeHandler(self)
        self.devnull.close()
        return self.logs



# Convert the InChI string to a Chem.Mol object
inchi = "InChI=1S/C49H66O10P2/c1-28(54-60-56-42-34(20-30(50-15)24-38(42)46(3,4)5)35-21-31(51-16)25-39(43(35)57-60)47(6,7)8)19-29(2)55-61-58-44-36(22-32(52-17)26-40(44)48(9,10)11)37-23-33(53-18)27-41(45(37)59-61)49(12,13)14/h20-29H,19H2,1-18H3/t28-,29-/m0/s1"

mol = Chem.inchi.MolFromInchi(inchi)

mol = Chem.AddHs(mol)
# Generate 3D coordinates for the molecule
with CaptureLogger() as capture:
    AllChem.EmbedMolecule(mol)

print(capture)
#AllChem.EmbedMolecule(mol)

#print(capture["WARNING"])

#AllChem.EmbedMolecule(mol)

print("hi")


# Get the 3D coordinates of the molecule
conf = mol.GetConformer()


# Make all the points multiple by -1
for i in range(conf.GetNumAtoms()):
    point = conf.GetAtomPosition(i)
    conf.SetAtomPosition(i, (-point.x, -point.y, -point.z))

# Update the conformer on the molecule object
mol.AddConformer(conf)

# Convert the molecule object back to an Inchi string
newinchi = Chem.inchi.MolToInchi(mol)

mol = Chem.inchi.MolFromInchi(newinchi)
mol = Chem.AddHs(mol)

# Loop through the atoms in the molecule and print their coordinates
for atom in mol.GetAtoms():
    idx = atom.GetIdx()
    pos = conf.GetAtomPosition(idx)
    print(f"Atom {idx}: {pos.x}, {pos.y}, {pos.z}")

