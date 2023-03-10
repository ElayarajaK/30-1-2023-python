#__ (private)
#_ (protected)

class Employee:
    __e_id=None;
    def __init__(self,e_id):
        self.e_id=e_id;


obj = Employee(201101);

print(obj.e_id)
        