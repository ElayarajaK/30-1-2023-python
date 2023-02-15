Tamil=int(input("Tamil marks"));
English=int(input("English marks"));
Science=int(input("Tamil marks"));
Math1=int(input("Tamil marks"));

fixed_marks=4*100;
total = Tamil+English+Science+Math1;
avg = total/4;
margin_marks=35;
Result="";
Gradepredict =0;

if( Tamil < margin_marks or English < margin_marks or Science < margin_marks or Math1 < margin_marks):
    if(Tamil < margin_marks):
        Result="Tamil marks",Tamil;
elif(Tamil > margin_marks and English > margin_marks and Math1 > margin_marks and Science > margin_marks):
    Total = Tamil+English+Math1+Science;
    avg = Total/4;
    Gradepredict=(Total/fixed_marks)*100;
    print("Tamil : ",Tamil,"English : ",English ,"Science ",Science,"Total" ,Total," % ",avg) 
    print("Grade :", Gradepredict)
    if(Gradepredict > 80):
        print(Gradepredict,"A Grade")
       
    



print(Result);