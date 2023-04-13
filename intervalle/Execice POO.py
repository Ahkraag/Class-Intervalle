class Intervalle:

    def __init__(self, a, b):
        self.setA(a)
        self.setB(b)

    def setA(self, n):
        self.a = n

    def getA(self):
        return self.a

    def setB(self, n):
        self.b = n

    def getB(self):
        return self.b

    def est_vide(self):
        return self.getB() < self.getA()

    def __len__(self):
        return max(0, self.getB() - self.getA())

    def __contains__(self, x):
        return self.getA() <= x <= self.getB()

    def __eq__(self, i):
        return self.est_vide() and i.est_vide() or self.getA() == i.a and self.getB() == i.b

    def __le__(self, i):
        return self.est_vide() or i.a <= self.getA() and self.getB() <= i.b

    def intersection(i, j):  # dans une classe une fonction est defini mais il n'y a pas self
        # c'est qu'on fait une méthode de classe, pour s'en servire il faut faire le nomdelaclasse.lamethode()
        return Intervalle(max(i.a, j.a), min(i.b, j.b))

    def __str__(self):
        res = "["
        if self.est_vide():
            return res + "]"
        else:
            res += str(self.getA()) + "," + str(self.getB())
            res += "]"
            return res

    def Union(i, j):
        return Intervalle(min(i.a, j.a), max(i.b, j.b))


#TEST#

a = Intervalle(206000000000, 8)
b = Intervalle(10, 15)
print(Intervalle.Union(a, b))