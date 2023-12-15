# Izmantojot teksta failā esošo informāciju nosākiet, 
# Kāds ir darbinieku skaits kas strādā telekomunikācijas jomā Latvijā.  (Industry = Telecommunications, Country = Latvia) ?
# Atbildes vietā ierakstiet tikai veselo skaitli.
get_info=input()
industry=input()
numberOfEmployees=[]
with open("data.txt", "r") as f:
        next(f)
        for line in f:
            row = line.rstrip().split(",")
            if row[4] == get_info and row[7] == industry:
                numberOfEmployees.append(int(row[8]))
# print(sorted(founded))
print(sum(numberOfEmployees))
# print(founded)