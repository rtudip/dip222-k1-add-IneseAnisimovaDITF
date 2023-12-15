# Izmantojot teksta failā esošo informāciju nosākiet:
# Kāds ir darbinieku skaits, kas strādā Latvijā?
# Atbildes vietā ierakstiet tikai veselo skaitli.
get_info=input()
numberOfEmployees=[]
with open("data.txt", "r") as f:
        next(f)
        for line in f:
            row = line.rstrip().split(",")
            # if row[5] == get_info:
            #     numberOfEmployees.append(int(row[9]))
            # faila apstrade nepareiza 365,6B0E704CD4b833D,"Castro, Maldonado and Beltran",http://www.baldwin.com/,Latvia,Persevering neutral info-mediaries,1986,Warehousing,7655
            if row[4] == get_info:
                 numberOfEmployees.append(int(row[8]))
print(sum(numberOfEmployees))