#####math:  *    |     +    |    -     |     **      |     /     |    //
num=int(input("enter a number with 4 digits: "))
alafim=num//1000
alafimm=alafim*1000
meott=num-alafimm
meot=meott//100
asarott=meot*100
asarottt=asarott+alafimm
asarotttt=num-asarottt
asarot=asarotttt//10
ahadott=asarot*10
ahadottt=alafimm+asarott+ahadott
ahadotttt=num-ahadottt
ahadot=ahadotttt//1





print("Alafim= " + str(alafim))
print("Meot= " + str(meot))
print("Asarot= " + str(asarot))
print("Ahadot= " + str(ahadot))