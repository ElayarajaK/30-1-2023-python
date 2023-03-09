class College:
    _c_name=None;
    _c_profit=5.5;
    def __init__(self,c_name,c_prfit):
        self._c_name=c_name;
        self._c_profit=c_prfit;
    def _printData(self):
        print(self._c_name,",",self._c_profit);
