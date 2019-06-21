dict={}
while True:
    print("_ _ _ _Birthday App _ _ _ _")
    print("1.Show Birthday")
    print("2.Add to Birthday list")
    print("3.Exit")
    choice=int(input("Enter the choice"))
    if choice==1:
        if len(dict.keys())==0:
            print("Nothing to show")

        else:
            name=input("Enter name to look for Birthday: ")
            birthday=dict.get(name,"No Data found")
            print(birthday)
    elif choice==2:
        name=input("Enter Friend's name: ")
        date=input("Enter birth date: ")
        dict[name]=date
        print("Birthday Added")
    elif choice==3:
        break
    else:
        print("Choose a VALID OPTION")
