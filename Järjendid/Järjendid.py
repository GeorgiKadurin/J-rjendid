#Самостоятельная работа 
список_вещей=[]
a=input(" ") #Придумай какие вещи можно взять с собой в поездку
slovo_list=list(a)
print(a)

while True:
    print("1-добавить предмет в список")
    print("2-добавить предмеи на x - позицию")
    print("3-удалить предмет")
    
    awp=int(input())
    if awp==1:
        r=input("Введите названия предмета:")
        a.append(r)
        print(f"Добавили {r} новый список", a)
    elif awp==2:
        r=input("Введите предмет, который хотите добавить: ")
        i=int(input("Введиту позицию, куда хотите добавить предмет: "))
        a.insert(i-1,r) #0,1,2,3,4,5...
        print(a)
    elif awp==3:
        r=input("Введи букву, которую хочешь удалить")
        g=a.count(a)
        if g>0:
           for i in range(g):
                a.remove(r)
        else:
            print("Искомой буквы нет")
        print(a)


           
print()
print()
spisok=[] #Пустой список
numbers=[1,2,3,4,5]
abc=["A", "B", "C"]
slovo="Programmeerimine"
slovo_list=list(slovo)
print(slovo)
print(slovo_list)

while True:
    print("1-добавить букву в список")
    print("2-склеить список\n3-добавить букву на i - позицию")
    print("4-удалить элемент")
   
    valik=int(input())
    if valik==1:
        a=input("Введи букву")
        slovo_list.append(a)
        print(f"Добавили {a} новый список", slovo_list)
    elif valik==2:
        slovo_list.extend(abc)
        print(slovo_list)
    elif valik==3:
        a=input("Введи букву, которую хочешь добавить")
        i=int(input("Введи позиции, куда хочешь добавить б"))
        slovo_list.insert(i-1,a) #0,1,2,3,4,5...
        print(slovo_list)
    elif valik==4:
        a=input("Введи букву, которую хочешь удалить")
        n=slovo_list.count(a)
        if n>0:
           for i in range(n):
                slovo_list.remove(a)
        else:
            print("Искомой буквы нет")
        print(slovo_list)








