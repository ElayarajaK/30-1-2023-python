from abc import *;

class car(ABC):
    @abstractmethod
    def noweels(self):
        pass
    @abstractmethod
    def Model(self):
        pass

class Tata(car):
    def noweels(self):
        print("4");
class Tatac(Tata):
    def Model(self):
        print("Hello Tiger")
       


#car = Tata();
car = Tatac();
car.noweels();
car.Model();