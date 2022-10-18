TeamA = ['Somchai','Somkiet','Daycha','Yodchai','Petch','Sopa']
TeamB = ['Nares','Sopa','Nipa','Daycha','Pimon','Petch']
TeamC = ['Choojai','Sopa','Somkiet','Nares','Nipa','Daycha','Tawan']
TeamD = ['Sopa','Tawan','Pimon','Yodchai','Petch','Somjai']

Reward = [0,5000,7500,10000,15000]


bar = "----------------------"
SetA = set(TeamA)
SetB = set(TeamB)
SetC = set(TeamC)
SetD = set(TeamD)

Uset = SetA | SetB | SetC | SetD

Mem4 = SetA & SetB & SetC & SetD
Mem3 = SetA & SetB & SetC - SetD | SetA & SetB & SetD - SetC
Me2 = SetA & SetB | SetA & SetC | SetA & SetD |\
       SetB & SetC | SetB & SetD | SetC & SetD
Mem2 = Me2 - Mem3 - Mem4
Mem1 = Uset - Mem4 - Mem3 - Me2
All_Mem = Mem4 | Mem3
print("REWARDS FOR SALE TEAM")
print(bar)
print("{0:14} {1:0}".format('Name','Reward'))
print(bar)
#..................................................................
for val in Mem4:
    print("{0:8} {1:12}".format(val,Reward[4]))
for val in Mem3:
    print("{0:8} {1:12}".format(val,Reward[3]))
for val in Mem2:
    print("{0:8} {1:12}".format(val,Reward[2]))
for val in Mem1:
    print("{0:8} {1:12}".format(val,Reward[1]))

#..................................................................
print(bar)
print("{0:14} {1:0}".format("Total","95,000"))
print(bar)