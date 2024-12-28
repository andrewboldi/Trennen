import os
from rdkit import Chem
from rdkit.Chem import AllChem
from tqdm import tqdm
import shutil

def GetEnantiomer(m):
  """ returns the enantiomer of a molecule. If an enantiomer does not exist, return None
   Arguments:
      - m: the molecule to work with
    >>> from rdkit import Chem
    >>> from rdkit.Chem.GetEnantiomer import GetEnantiomer
    >>> m = Chem.MolFromSmiles('CN1CCC[C@H]1C2=CN=CC=C2') # L-(-)-Nicotine
    >>> Chem.MolToSmiles(GetEnantiomer(m)) # (+)-Nicotine
    CN1CCC[C@@H]1C2=CN=CC=C2
    If an enantiomer does not exist (i.e. the molecule is not chiral), None will be returned
    >>> m = Chem.MolFromSmiles('[C@@H]([C@@H](C(=O)O)O)(C(=O)O)O') # meso-Tartaric Acid
    >>> GetEnantiomer(m)
    None
  """


  m1 = Chem.AddHs(m)
  AllChem.EmbedMolecule(m1) # Make sure molecule is in 3D
  m_b = Chem.MolToMolBlock(m1)

  # Reflect the molecule across the origin
  m_b = m_b.replace("-", "+").replace("    ", "   -").replace("+", " ")
  m2 = Chem.MolFromMolBlock(m_b)

  # If an enantiomer does not exist, return None
  if Chem.MolToSmiles(m1) == Chem.MolToSmiles(Chem.AddHs(m2)):
      return None

  return m2

def GetChirality(m):
  """ returns the chirality of a molecule. Return True if the molecule is chiral and False if it is not. 
   Arguments:
      - m: the molecule to work with
    >>> from rdkit import Chem
    >>> from rdkit.Chem.GetChirality import GetChirality
    >>> m = Chem.MolFromSmiles('CN1CCC[C@H]1C2=CN=CC=C2') # L-(-)-Nicotine
    >>> GetChirality(m)
    True
    If a molecule is achiral (not chiral), the function will return False
    >>> m = Chem.MolFromSmiles('[C@@H]([C@@H](C(=O)O)O)(C(=O)O)O') # meso-Tartaric Acid
    >>> GetChirality(m)
    False
  """

  if GetEnantiomer(m) == None:
      return False
  else:
      return True

out_file = open("CHIRAL_FILES.txt", "a")
for file_ in tqdm(os.listdir("files_with_chiral_centers/files")):
    my_file = open("files_with_chiral_centers/files/" + file_, "r")
    lines = my_file.readlines()
    base_smile = lines[len(lines) - 2].split("\t")[1].split("\n")[0]
    try:
        if (b := GetEnantiomer(Chem.MolFromSmiles(base_smile))) is not None:
            
            shutil.copy("files_with_chiral_centers/files/" + file_, "files_with_chirality/files/" + file_)
            out_file.write(base_smile + "\n")
            out_file.write(Chem.MolToSmiles(b) + "\n")
    except:
        pass

    my_file.close()

