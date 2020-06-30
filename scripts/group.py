import random

#関数の定義
def Amida(low, high):
    teamList = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
    for num in range(low,high+1,1):
        team = teamList.pop(random.randrange(0,len(teamList),1))
        print('{:02}'.format(num), team, sep='-----')

print('男子チーム')
Amida( 1,11)
Amida(12,22)
Amida(23,32)

print()
print('女子チーム')
Amida( 1,11)
Amida(12,22)
Amida(23,31)
