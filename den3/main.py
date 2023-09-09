hodnoty = open('hodnoty.txt').read().splitlines()
#print (hodnoty)
global epsilon
global gamma
global count_1
global count_0
count_0 =0
count_1 =0
epsilon =0
gamma = 0
tmp = range(len (hodnoty[1]))
#print(tmp)
#delka_cisla = len (hodnoty[1])
#print (delka_cisla)

if __name__ == '__main__':
    for x in tmp:
        for hodnota in hodnoty:
            if hodnota[x] == "0":
                count_0 = count_0 + 1
                #print ("byla nula")
            else:
                count_1 = count_1 + 1
                #print ("byla jedna")
        gamma *= 2
        epsilon *= 2
        if count_1 > count_0:
            gamma = gamma +1
            print("vice jednicek")

        else:
            epsilon = epsilon +1
            print("vice nul")
        count_0=0
        count_1 = 0


    print (epsilon*gamma)
