# 4)შემოაყვანინე მომხმარებელს ელემენტი თუ 
# ინტეჯერია ჩაამატე ლისტში თუ არა და ლისტის ბოლო ელემენტი წაშალე.


lst = ["zura","nikolz","dachi"]
el = input("enter element: ")
if el.isdigit():
    lst.append(el)
elif el:
    lst.remove("elene")

print(lst)