tomato=int(input("tomato number: "))
cucumber=int(input("cucumber number: "))
coke=int(input("coke number: "))
chicken=int(input("chicken kg number: "))

cost=((tomato*3) + (cucumber*2) + (coke*5) + (chicken*20))
print("cost without tax: " + str(cost) + " nis")
print("cost with tax: " + str("%.1f" % (cost*1.17)) + " nis")


