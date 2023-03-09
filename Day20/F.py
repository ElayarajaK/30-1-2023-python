from E import College;
#from D import A;

#obj = College();

#obj = A("raja",20111);

#print("from f : ",obj.__name)

class staff(College):
    def __init__(self, c_name, c_prfit):
        super().__init__(c_name, c_prfit)

    def _printData(self):
        print(self._c_name);

obj = staff("niit",2022);
obj._printData();