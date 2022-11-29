class Sotrudnik:
    ruClassName = "None"
    objInstancesCount = 0

    def __init__(self, name, doljnost, oklad):
        self._name = name
        self.id = doljnost
        self.age = oklad
        Sotrudnik.objInstancesCount = Sotrudnik.objInstancesCount + 1


    def get_name(self):
        return self._name

    def set_name(self, n):
        self._name = n

    def info(self):
        print(self._name)
        print("Doljnost: " + str(self.id))
        print("Oklad: " + str(self.age))

class Maneger(Sotrudnik):
    def __init__(self,):
