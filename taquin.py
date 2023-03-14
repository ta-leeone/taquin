import random


class Position :
     x :int 
     y :int 
     def __init__(self, x, y) :
        self.x = x
        self.y = y

     def getX(self) :
        return self.x
     def getY(self) :
        return self.y
     def setX(self, x) :
        self.x = x
     def setY(self, y) :
        self.y = y
        def clone(self):
            return Position(self.x, self.y)




class CaseVide:
    Position:Position
    taquin:Taquin
    value:int
    def __init__(self, position, taquin) :
        self.position = position
        self.taquin = taquin


    def getPositionX(self) :
        return self.position.getX()
    def setPositionX(self, positionX) :
        self.position.setX(positionX)

    def getPositionY(self) :
        return self.position.getY()
    def setPositionY(self, positionY) :
        self.position.setY(positionY)

    def getTaquin(self) :
        return self.taquin
    def setTaquin(self, taquin) :
        self.taquin = taquin
    def getValue(self) :
        return None
    def setValue(self, value) :
        pass
    def clone(self):
        return CaseVide(self.position, self.taquin)
    def moveNorth(self, direction)->bool:
        if direction == "N" :
            if self.position.getY() > 0 :
               
                caseADescendre=self.taquin.getCase(self.position.getX(), self.position.getY() + 1)
                caseADescendre.setPositionY(self.position.getY())
                self.position.setY(self.position.getY() + 1)
                self.taquin.setCase(self.position.getX(), self.position.getY(), self)
                self.taquin.setCase(caseADescendre.getPositionX(), caseADescendre.getPositionY(), caseADescendre)
                return True
        return False
    def moveSouth(self, direction)->bool:
        if direction == "S" :
            if self.position.getY() < self.taquin.getSize() - 1 :
                caseARemonter=self.taquin.getCase(self.position.getX(), self.position.getY() - 1)
                caseARemonter.setPositionY(self.position.getY())
                self.position.setY(self.position.getY() - 1)
                self.taquin.setCase(self.position.getX(), self.position.getY(), self)
                self.taquin.setCase(caseARemonter.getPositionX(), caseARemonter.getPositionY(), caseARemonter)
                return True
        return False
    def moveEast(self, direction)->bool:
        if direction == "E" :
            if self.position.getX() < self.taquin.getSize() - 1 :
                caseADroite=self.taquin.getCase(self.position.getX() + 1, self.position.getY())
                caseADroite.setPositionX(self.position.getX())
                self.position.setX(self.position.getX() + 1)
                self.taquin.setCase(self.position.getX(), self.position.getY(), self)
                self.taquin.setCase(caseADroite.getPositionX(), caseADroite.getPositionY(), caseADroite)
                return True
        return False
    def moveWest(self, direction)->bool:
        if direction == "W" :
            if self.position.getX() > 0 :
                caseAGauche=self.taquin.getCase(self.position.getX() - 1, self.position.getY())
                caseAGauche.setPositionX(self.position.getX())
                self.position.setX(self.position.getX() - 1)
                self.taquin.setCase(self.position.getX(), self.position.getY(), self)
                self.taquin.setCase(caseAGauche.getPositionX(), caseAGauche.getPositionY(), caseAGauche)
                return True
        return False






class Case(CaseVide):
    
    
   
    def __init__(self, value, position, taquin) :
        self.value = value
        self.position = position
        self.taquin = taquin

    def getValue(self) :
        return self.value
    def setValue(self, value) :
        self.value = value

    def moveNorth(self, direction)->bool:
        if direction == "N" :
         return False
    def moveSouth(self, direction)->bool:
        if direction == "S" :
         return False
    def moveEast(self, direction)->bool:
        if direction == "E" :
         return False
    def moveWest(self, direction)->bool:
        if direction == "W" :
         return False
    def clone(self):
        return Case(self.value, self.position.clone(), self.taquin)







class listePriorite:
    def __init__(self,taquinFinal:'Taquin',poids:list(int)):
        self.liste = []
        self.taquinFinal=taquinFinal
        self.poids=poids
    def insert(self, element,comparator):
        if len(self.liste) == 0:
            self.liste.append(element)
        else:
            for i in range(len(self.liste)):
                if comparator(self.liste[i],self.taquinFinal,self.poids):#element.comparator() - self.liste[i].comparator()<0
                    self.liste.insert(i, element)
                    break
                elif i == len(self.liste) - 1:
                    self.liste.append(element)
                    break
    def pop(self):
        return self.liste.pop(0)
    def isEmpty(self):
        return len(self.liste) == 0






class Taquin:
    size :int
    cases:list(list(CaseVide))
    CaseVide:CaseVide
    def __init__(self, size,parent:'Taquin') :
        z=0
        self.size = size
        self.parent = parent
        for i in range(size):
            self.cases.append([])
            for j in range(size):
                if(j==size-1 and i==size-1):
                    caseVide=CaseVide(Position(i, j), self)
                    self.cases[i].append(caseVide)
                    z+=1
                    break
                self.cases[i].append(Case(z,Position(i, j), self))
                z+=1
   
    def __init__(self, taquin:"Taquin"):
        self.size = taquin.size
        self.parent = taquin.parent

        for i in range(self.size):
            self.cases.append([])
            for j in range(self.size):
                self.cases[i].append(taquin.cases[i][j].clone())
                if self.cases[i][j].getValue() == 0:
                    self.CaseVide = self.cases[i][j]
        

    def getSize(self) :
        return self.size
    
    def getCase(self, x, y) :
        return self.cases[x][y]
    def getCase(self,val):
        for i in range(self.size):
            for j in range(self.size):
                if self.cases[i][j].getValue() == val:
                    return self.cases[i][j]
                
    def setCase(self, x, y, case) :
        self.cases[x][y] = case
    def getCaseVide(self) :
        return self.CaseVide
    def getParent(self) :
        return self.parent
    def cout(self):
        return self.parent.cout()+1#fonction g
    
    def move(self, direction) :
        return self.CaseVide.move(direction)
    
    def isSolved(self,taquinFinal:'Taquin') :
        for i in range(self.size):
            for j in range(self.size):
                if self.cases[i][j].getValue() != taquinFinal.cases[i][j].getValue():
                    return False
        return True
    
    def __str__(self) :
        res = ""
        for i in range(self.size):
            for j in range(self.size):
                res += str(self.cases[i][j].getValue()) + " "
            res += "\n"

        return res
    
    def clone(self) :
        return Taquin(self)
    
    def distmanhattan(self, taquinFinal:'Taquin',i:int,j:int) :
        
        c=self.cases[i][j]
        if c.getValue() != None:
                    cFinal=taquinFinal.getCase(c.getValue())
                    return abs(c.getPosition().getX() - cFinal.getPosition().getX()) + abs(c.getPosition().getY() - cFinal.getPosition().getY())
        return 0#A revoir pour la case vide
   
   
   
    def shuffle(self, nbMoves:int):
        for i in range(nbMoves):
            self.move(random.choice(["N", "S", "E", "W"]))

    def heuristiquePondere(self,taquinFinal:'Taquin',poids:list(int)):
        res=0
        for i in range(self.size):
            for j in range(self.size):
                res+=self.distmanhattan(taquinFinal,i,j)*poids[self.cases[i][j].getValue()]
        return res
    def fnctEval(self,taquinFinal:'Taquin',poids:list(int)):
        return self.heuristiquePondere(taquinFinal,poids)+self.cout()

    def getVoisins(self,taquinFinal:'Taquin',poids:list(int))->list('Taquin'):
        voisins:list(Taquin)=[]
        for direction in ["N", "S", "E", "W"]:
            if self.move(direction):
                voisins.append((self.clone(),self.fnctEval(taquinFinal,poids)))
                self.move(self.getOppositeDirection(direction))
        return voisins
    def getOppositeDirection(self,direction):
        if direction == "N":
            return "S"
        elif direction == "S":
            return "N"
        elif direction == "E":
            return "W"
        elif direction == "W":
            return "E"
        return None
   
    def compareTo(self, taquin:'Taquin',taquinFinal:'Taquin',poids:list(int)) :
        return self.fnctEval(taquinFinal,poids) - taquin.fnctEval(taquinFinal,poids)
    def solve(self, taquinFinal:'Taquin',poids:list(int)) :
        openList = listePriorite()
        closedList:list(Taquin) = []
        openList.insert(self, self.fnctEval(taquinFinal,poids))
        while not openList.isEmpty():
            current:Taquin = openList.pop()
            if current.isSolved(taquinFinal):
                return current
            closedList.append(current)
            for voisin in current.getVoisins(taquinFinal,poids):
                if voisin[0] not in closedList:
                    openList.insert(voisin[0],voisin.compareTo)
        return None

