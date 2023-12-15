# Izmantojot teksta failā esošo informāciju nosākiet:
# Cik no datu bāze esošajiem Latvijas kompānijām ir SSL sertifikāts? (SSL sertifikāts ir kompānijām, kuram tīmekļa adrese sākas ar https://)
# Atbildes vietā ierakstiet tikai veselo skaitli.
get_info=input()
ssl=[]
with open("data.txt", "r") as f:
        next(f)
        for line in f:
            row = line.rstrip().split(",")
            if row[4] == get_info:
                ssl.append((row[3]))
print((ssl))
