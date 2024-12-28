import os

done = 0
mols = []

for molecule in os.listdir("inp"):
    try:
        lastline = open(f"inp/{molecule}/{molecule}.out").readlines()[-1]
    except:
        continue
    if "TOTAL RUN TIME" in lastline:
        done += 1
        mols.append(int(molecule))

print(done)
print(sorted(mols))
