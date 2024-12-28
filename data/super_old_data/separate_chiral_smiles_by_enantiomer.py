my_file = open("CHIRAL_SMILES.txt", "r")
lines = my_file.readlines()
o1 = open("CHIRAL_SMILES_1.txt", "a")
o2 = open("CHIRAL_SMILES_2.txt", "a")

for i in range(0, len(lines), 2):
    o1.write(lines[i])
    o2.write(lines[i+1])

o1.close()
o2.close()
my_file.close()
