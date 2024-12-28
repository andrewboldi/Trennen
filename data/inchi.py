data = open("iloveinchi.txt").readlines()

for i, inchi in enumerate(data):
    out = open(f"inchi2/{i:0>5}.inchi", "w")
    out.write(inchi.split(", ")[0])
    out.close()
    
