class TATA:
    _bname=None;
    def __init__(self,bname):
        self._bname=bname;


class TCS(TATA):
    def __init__(self, bname):
        pass;


obj =TCS("IT Services");

print(obj._bname)