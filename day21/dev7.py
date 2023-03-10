class TATA:
    Name ="Rathan";
    Main_Office="Mumbai";

class TCS(TATA):
    RM_Name="Dhinesh";
    TCS_profit=6.7;
class TPower(TCS):
    Manager="Jhon";
    TProfit =8.9;

obj = TPower();

print(obj.Name,",",obj.Main_Office,",",obj.RM_Name,",",obj.TCS_profit,",",obj.Manager,",",obj.TProfit)
