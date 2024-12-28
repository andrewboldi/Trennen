from rdkit import Chem
from pypointgroup import PointGroup

smiles = 'CC(C)(C)C(O)=O'

mol = Chem.MolFromSmiles(smiles)

pg = PointGroup.from_molecule(mol)
print(f'Point group symmetry: {pg.symmetry_type}')
