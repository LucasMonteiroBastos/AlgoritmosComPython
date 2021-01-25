print('quantos gols o flamengo fez? ')
a = int(input())
print('quantos gols o vasco fez? ')
b = int(input())
dif = a - b
status = 0
if dif >= 1 and dif <= 3:
    status = 'PARTIDA NORMAL'
elif dif == 0:
    status = 'EMPATE'
elif dif >= 4:
    status = 'GOLEADA'

print('DIFERENÇA: {}'.format(dif))
print('STATUS: {}'.format(status))