import random
n         =int(input("Enter the number of the cities : "))
hot       = []
mild      =[]
cool      =[]
freezing  =[]
x=0
list      =[]
while len(list)!=n:
    list.append(random.uniform(-15,45))
    x=x+1
print(list)
print()
h_counter =0
m_counter =0
c_counter =0
f_counter =0
while m!=n:
    if  list[m]>=28 and list[m]<=45:
        hot.append(list[m])
        h_counter=h_counter+1
    elif  list[m]>=15 and list[m]<=27.9:
        mild.append(list[m])
        m_counter=m_counter+1
    elif  list[m]>=4 and list[m]<=14.9:
        cool.append(list[m])
        c_counter=c_counter+1
    elif  list[m]>=-15 and list[m]<=3.9:
        freezing.append(list[m])
        f_counter=f_counter+1
    m=m+1
        
print("Temp Category""                        ""Count""                                                                 ""List of temp in this category")
print("______________________________________________________________________________________________________________________________________________________________________________")
print()
print ("Hot",f"                                          {h_counter}                                                                      {hot}")
print ("Mild",f"                                        {m_counter}                                                                      {mild}")
print ("Cool",f"                                        {c_counter}                                                                      {cool}")




a="Rice 10kg"
b=47

c="Atta 1 kg"
d=47

e="Lemon 4pc"
f=39

g="Carrot 50g"
h=29

i="Onion 1 kg"
j=29

k="Brinjal 500g"
l=49

m="King Potato 1kg"
n=20

print ("Product No""                               ""Product Name""                    ""Product Price(Tk)")
print( "_________""                                    ""_________________""                  "" _____________________")
print()
print("1"f"                                                 {a}                                        {b}             ")
print("2"f"                                                 {c}                                         {d}             ")
print("3"f"                                                 {e}                                      {f}             ")
print("4"f"                                                 {g}                                      {h}             ")
print("5"f"                                                 {i}                                      {j}             ")
print("6"f"                                                 {k}                                     {l}             ")
print("7"f"                                                 {m}                               {n}             ")





