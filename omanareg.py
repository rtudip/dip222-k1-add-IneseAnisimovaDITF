# Izmantojot teksta failā esošo informāciju nosākiet:
# Kurā gadā bija dibināts vecākais Omānas reģiona uzņēmums (informācija ir pieejama kolonnā Founded)?
# Atbildes vietā ierakstiet tikai veselo skaitli.
get_info=input()
founded=[]
with open("data.txt", "r") as f:
        next(f)
        for line in f:
            row = line.rstrip().split(",")
            if row[4] == get_info:
                founded.append(int(row[6]))
# print(sorted(founded))
print(min(founded))
# print(founded)