my_file = open("CHIRBASE_SEPARATION.txt", "r")
lines = my_file.readlines()
out_file = open("CHIRBASE_SEPARATION_UPDATED.txt", "a")

for i, line in enumerate(lines):
    try:
        if lines[i] != lines[i+1]:
            out_file.write(lines[i])
    except:
        out_file.write(lines[i])

my_file.close()
out_file.close()
