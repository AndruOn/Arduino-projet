



        
def posxy(l):
    n= len(l)
    maxun= 0
    maxdeux= 0
    pos=[0,0]
    for i in range(n):
        if l[i] >= maxun:
            maxdeux= maxun
            maxun= l[i]
    maxi= l.index(maxun)
    maxdeuxi= l.index(maxdeux)
    print("maxun= ",maxun," index= ",maxi)
    print("maxdeux= ",maxdeux," index= ",maxdeuxi)
    
    if maxi >= maxdeuxi:
        if abs(maxdeuxi-maxi)== 1:     ##horiontal
            disthoriz= maxdeux / maxun
            pos[0]= maxi % 3 + disthoriz
            print("posx= ",pos[0])
            a= maxi + 3
            b= maxi - 3
            if a <= 9 and 0 <= b :
                if l[a] >= l[b]:              ##vertical
                    distvertic= l[b] / l[a]
                    pos[1]= a // 3 - distvertic
                    print("posy= ",pos[1])
                else:
                    distvertic= l[a] / l[b]
                    pos[1]= a // 3 + distvertic
                    print("posy= ",pos[1])
            else:
                if a <= 9:
                    distvertic= a / maxun
                    pos[1]= maxun  
                    
                
                
            return pos                            
        
        elif abs(maxdeuxi-maxi)== 3:    ##vertical
            distvertic= maxdeux / maxun
            pos[1]= maxi // 3 - distvertic
            
            
    else:
        if abs(maxdeuxi-maxi)== 1:     ##horiontal
            disthoriz= maxdeux / maxun 
            pos[0]= maxi % 3 - disthoriz
         
        elif abs(maxdeuxi-maxi)== 3:   #vertical
            distvertic= maxdeux / maxun
            pos[1]= maxi // 3 + distvertic
    

    
def pos_tri(l):
    n= len(l)
    maxa= max(l)
    maxi= l.index(maxa)
    print("maxun= ",maxa," index= ",maxi)
    dico= dic[maxi]
    index_voisins=dico.values()
    print(index_voisins)
    if len(index_voisins)==2:
        return "formule"
    
        
        
dic={
    0:{"droite":1,"bas":3},
    1:{"gauche":0,"droite":2,"bas":4},
    2:{"gauche":1,"bas":5},
    3:{"haut":0,"droite":4,"bas":6},
    4:{"gauche":3,"haut":1,"droite":5,"bas":7},
    5:{"gauche":4,"haut":2,"bas":8},
    6:{"haut":3,"droite":7},
    7:{"gauche":6,"haut":4,"droite":8},
    8:{"gauche":7,"haut":5},
        }
    
    
    
    
    
    
    
    
    
    
    
    
    
l1= [2,2,4,15,20,1,3,4,2]
l2= [12,13,5,3,2,1,0,1,0]
l3= [2,0,0,7,8,18,1,5,15]
l= [l1,l2,l3]

for liste in l:
    print("liste= %s" % (liste))
    print("---------------technique 1---------------")
    print("position: ",posxy(liste))
    print("---------------technique 2---------------")
    print("position: ",pos_tri(liste))
    print() 

print(" 0  1  2")
print(" 3  4  5")
print(" 6  7  8")