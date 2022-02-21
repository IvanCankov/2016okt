def idobe(self):
    return str(self // 3600) + ' ' + str(self % 3600 // 60) + ' ' + str(self % 60)

def mpbe(o,p,mp):
    return o * 3600 + p * 60 + mp

hivasok = []

with open('hivas.txt') as file:
    for line in file:
        parts = [int(item) for item in line.strip().split()]
        hivas = {}
        hivas['eleje'] = mpbe(*parts[:3])
        hivas['vege'] = mpbe(*parts[3:])
        hivas['hossza'] = hivas['vege'] - hivas['eleje']
        hivasok.append(hivas)

print('3. feladat')
statisztika = {}
for hivas in hivasok:
    ora = idobe(hivas['eleje']).split()[0]
    #statisztika[ora] = statisztika.get(ora, 0) + 1
    if ora not in statisztika:
        statisztika[ora] = 1
    else:
        statisztika[ora] += 1

for key, value in statisztika.items():
    print(f"{key} {value}")

print('4. feladat')
leghosszabb = max(hivasok, key = lambda x: x['hossza'])
print(f"{leghosszabb['hossza']}")

print('5. feladat')
idopont = input('Adjon meg egy idopontot: ')
idopont = mpbe(*[int(elem) for elem in idopont.split(' ')])
print(idopont)
