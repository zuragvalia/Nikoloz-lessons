# classwork:1)მომხმარებელს შემოატანინე მისი შემაფასებელი ქულა (0-დან 100-ის ჩათვლით).

#  იმ შემთხვევაში თუ შემოტანილი ქულა მეტია ან ტოლია 90-ის, ტერმინალში გამოიტანე "Grade A".
#  თუ მისი ქულა მეტია ან ტოლია 70-ზე გამოიტანე "Grade B". 
#  თუ მომხმარებლის ქულა მეტია ან ტოლია 50-ზე ტერმინალში დაბეჭდე "Grade C"
#  ყველა დანარჩენ შემთხვევაში გამოიტანე  "Grade F"


grade = int(input("enter your grade"))
if 100 < grade > 0:
    print("enter a new number")
if 100 >= grade >= 90:
    print("Grade A")
if 90 > grade >= 70:
    print("Grade B")
if 70 > grade >= 50:
    print("Grade C")
if 50 > grade > 0:
    print("Grade F")
else:
    print

