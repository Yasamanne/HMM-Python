__author__ = 'yasamanemami'


def main():
    transition_model = [[]]
    transition_model = [[0 for i in range(6)] for j in range(6)]
    for i in range (0,6):
        for j in range (0,6):
            if i == j:
                transition_model [i][j] = 0.3
            if i - j == -1:
                transition_model [i][j] = 0.7
    transition_model [5][0] = 0.7

    #print(transition_model)


    observation_model = [[]]
    observation_model = [[0 for i in range(6)] for j in range(6)]
    for i in range (0,6):
        for j in range (0,6):
            if i == j :
                observation_model [i][j] = 0.8
            if abs(i - j) == 1:
                observation_model [i][j] = 0.1
    observation_model [0][0] = 0.9
    observation_model [5][5] = 0.9
    #print(observation_model)

    Names = ['DinklageLives','Strider','Thundercat','Sigaldry','LaborDay']
    obsBuSF_Train = [ [3,5,4,0,1,1,3,2,3,4],
                      [4,4,5,0,1,2,3,4,5,0],
                      [1,1,3,4,5,0,1,2,3,3],
                      [3,3,4,4,0,1,0,1,2,3],
                      [4,5,0,0,0,2,2,3,4,4]]

    #print(obsBuSF_Train[0][0])
    I = []
    L = []
    start_probability = 0.16
    for k in range (5):         # horses numbers
        for j in range (10):    # 10 race observation 10 refines
            for i in range (6): # 6states based on trasition model p(BuSF)
                pBuSF = 0
                for m in range (6):
                    if j == 0 : #predict state1
                        q = start_probability
                    else:
                        o = (60*k)+(6*(j-1))+m
                        q = L[o]
                    pBuSF =  pBuSF + q * transition_model[m][i]
                I.extend([pBuSF])
            #print (I)

            y = obsBuSF_Train [k][j]
            for i in range (6): # 6states based on trasition model p(BuSF)
                s = 0
                for m in range (6):
                    u = (60*k)+(6*j)+m
                    #print ('u')
                    #print (u)
                    s = s + (observation_model[y][m] * I[u])
                #print (s)
                p = (60*k)+(6*j)+i
                z = (observation_model[i][y] * I[p])/s
                L.extend([z])
    print ('Predict states',I)
    print ('Refine states',L)


    pBuSF_final_predict =[]
    for i in range (6):
        pBuSF = 0
        for j in range (6):
            pBuSF =  pBuSF + L[294+j] * transition_model[j][i]
        pBuSF_final_predict.extend ([pBuSF])
    print('LaborDays final predict',pBuSF_final_predict)
    pBuSF_obsfinal_predict =[]
    for i in range (6):
        pBuSF = 0
        for j in range (6):
            pBuSF =  pBuSF + pBuSF_final_predict[j] * observation_model[j][i]
            #print ('pBuSF',pBuSF)
        pBuSF_obsfinal_predict.extend ([pBuSF])
        #T =0
        #for i in range (1,7):
            #T = T + i* pBuSF_obsfinal_predict[i-1]
    print('LaborDay BuSF',pBuSF_obsfinal_predict)
    #v=max(pBuSF_obsfinal_predict)
    T = 0
    for i in range (6):
        T = T + i*(pBuSF_obsfinal_predict[i])
    print ('""LaborDay expobsBuSF"":',T)
    #print ('max probability of obs:',v)
    #print('expObsBuSF LaborDay:',pBuSF_obsfinal_predict.index(v))


    pBuSF_final_predict =[]
    for i in range (6):
        pBuSF = 0
        for j in range (6):
            pBuSF =  pBuSF + L[254+j] * transition_model[j][i]
        pBuSF_final_predict.extend ([pBuSF])
    print('Sigaldry final predict',pBuSF_final_predict)
    pBuSF_obsfinal_predict =[]
    for i in range (6):
        pBuSF = 0
        for j in range (6):
            pBuSF =  pBuSF + pBuSF_final_predict[j] * observation_model[j][i]
            #print ('pBuSF',pBuSF)
        pBuSF_obsfinal_predict.extend ([pBuSF])
    print('Sigaldry BuSF',pBuSF_obsfinal_predict)
    T = 0
    for i in range (6):
        T = T + i*(pBuSF_obsfinal_predict[i])
    print ('""Sigaldry expobsBuSF:""',T)
    #v=max(pBuSF_obsfinal_predict)

    #print ('max probability of obs:',v)
    #print('expObsBuSF Sigaldry:',pBuSF_obsfinal_predict.index(v))


    pBuSF_final_predict =[]
    for i in range (6):
        pBuSF = 0
        for j in range (6):
            pBuSF =  pBuSF + L[174+j] * transition_model[j][i]
        pBuSF_final_predict.extend ([pBuSF])
    print('Thundercat final predict',pBuSF_final_predict)
    pBuSF_obsfinal_predict =[]

    for i in range (6):
        pBuSF = 0
        for j in range (6):
            pBuSF =  pBuSF + pBuSF_final_predict[j] * observation_model[j][i]
            #print ('pBuSF',pBuSF)
        pBuSF_obsfinal_predict.extend ([pBuSF])
    print('Thundercat BuSF',pBuSF_obsfinal_predict)
    T = 0
    for i in range (6):
        T = T + i*(pBuSF_obsfinal_predict[i])
    print ('""Thundercat expobsBuSF:""',T)
    #v=max(pBuSF_obsfinal_predict)

    #print ('max probability of obs:',v)
    #print('expObsBuSF Thundercat:',pBuSF_obsfinal_predict.index(v))

    pBuSF_final_predict =[]
    for i in range (6):
        pBuSF = 0
        for j in range (6):
            pBuSF =  pBuSF + L[114+j] * transition_model[j][i]
        pBuSF_final_predict.extend ([pBuSF])
    print('Strider final predict',pBuSF_final_predict)
    pBuSF_obsfinal_predict =[]

    for i in range (6):
        pBuSF = 0
        for j in range (6):
            pBuSF =  pBuSF + pBuSF_final_predict[j] * observation_model[j][i]
            #print ('pBuSF',pBuSF)
        pBuSF_obsfinal_predict.extend ([pBuSF])
    print('Strider BuSF',pBuSF_obsfinal_predict)
    #v=max(pBuSF_obsfinal_predict)
    T =0
    for i in range (6):
        T = T + i*(pBuSF_obsfinal_predict[i])
    print ('""Strider expobsBuSF:""',T)


    #print ('max probability of obs:',T)
    #print('expObsBuSF Strider:',pBuSF_obsfinal_predict.index(v))

    pBuSF_final_predict =[]
    for i in range (6):
        pBuSF = 0
        for j in range (6):
            pBuSF =  pBuSF + L[54+j] * transition_model[j][i]
        pBuSF_final_predict.extend ([pBuSF])
    T =0
    for i in range (6):
        T = T + i*(pBuSF_obsfinal_predict[i])
    print('DinklageLives final predict',pBuSF_final_predict)
    pBuSF_obsfinal_predict =[]
    #print(T)
    for i in range (6):
        pBuSF = 0
        for j in range (6):
            pBuSF =  pBuSF + pBuSF_final_predict[j] * observation_model[j][i]
            #print ('pBuSF',pBuSF)
        pBuSF_obsfinal_predict.extend ([pBuSF])
    print('DinklageLives BuSF',pBuSF_obsfinal_predict)
    #v=max(pBuSF_obsfinal_predict)
    T =0
    for i in range (6):
        T = T + ((i)*(pBuSF_obsfinal_predict[i]))
       # print(T)
    print ('""DinklageLives expobsBuSF:""',T)
    #print('expObsBuSF DinklageLives:',pBuSF_obsfinal_predict.index(v))
    #print(T)

if __name__ == "__main__":
             main()

