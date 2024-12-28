# Data

Ground Truth:
- We have a file "ilovesmiles.txt" with smiles strings of molecules with chiral centers

Let's use transformers? 

Attaining Truth:
+ 0. What are the InChI strings?
+ 1. Which molecules are chiral?
+ 2. Which molecules have optical rotation markers?
+ 3. What is its optical direction?
+ 4. Is its enantiomer in the dataset?
+ 5. No? Add it and label it the opposite direction.

Done! Got the data!

## Notes
- Spent a lot of time spinning my wheels on trying to use SMILES
- But this does not work well since it is not a good way to identify if the two molecules are the same.
- When I first first first had this idea, I came across InChI and then disregarded it...
- In hindsight, I now see InChI is good because each molecule has a unique inchi string and also encodes 3-D info.
- Yes, there is a 44 molecule difference in "ilovedata.txt"... but I could not find a bug in it after spending half a day on it.
- Spent WAY too much time using rdkit. Also it was super slow. Openbabel is 100x better
