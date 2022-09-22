import mysql.connector as sql
import tabulate
conn=sql.connect(host='localhost',user='root',passwd='root',database='project')
c=conn.cursor()
c.execute("select * from Types_of_Appliances ")
table1=tabulate.tabulate(c,headers=["Sr.No.", "Type of Appliance", "Number of Models Available", "Price Range"],tablefmt="psql")
c.execute("select  *  from washing_machines")
table2=tabulate.tabulate(c,headers=["Sr.No.", "Name" , "Sale price" , "MRP and discount" , "Warranty duration"],tablefmt="psql")
c.execute("select * from microwave_ovens")
table3=tabulate.tabulate(c,headers=["Sr.No.","Name" , "Sale price" , "MRP and discount" , "Warranty duration"],tablefmt="psql")
c.execute("select * from air_conditioners")
table4=tabulate.tabulate(c,headers=["Sr.No.","Name" , "Sale price", "MRP and discount" , "Warranty duration" , "Rating"],tablefmt="psql")
c.execute("select * from chimneys") 
table5=tabulate.tabulate(c,headers=["Sr.No." , "Name" , "Sale price", "MRP and discount" , "Warranty duration" ,"Suction capacity" ],tablefmt ="psql")
c.execute("select * from  refrigerators ")
table6=tabulate.tabulate(c,headers=["Sr.No." ,"Name" , "Sale price", "MRP and discount" , "Warranty duration" ,"Rating"],tablefmt="psql")



print('''__        __ _____  _       ____   ___   __  __  _____ 
\ \      / /| ____|| |     / ___| / _ \ |  \/  || ____|
 \ \ /\ / / |  _|  | |    | |    | | | || |\/| ||  _|  
  \ V  V /  | |___ | |___ | |___ | |_| || |  | || |___ 
   \_/\_/   |_____||_____| \____| \___/ |_|  |_||_____|''')
print("\n")
print(''' _____   ___  
|_   _| / _ \ 
  | |  | | | |
  | |  | |_| |
  |_|   \___/ 
              ''')
print("\n")
print(''' ___  _   _  ___  _____  ___   _   _ 
|_ _|| \ | ||_ _||__  / / _ \ | \ | |
 | | |  \| | | |   / / | | | ||  \| |
 | | | |\  | | |  / /_ | |_| || |\  |
|___||_| \_||___|/____| \___/ |_| \_|''')
print("\n")

complete='n'
while complete == 'n':
    print('\n')
    print(table1)
    print('ALL PRICES ARE IN INR')
    print('\n')

    def inp():
        x=int(input("\nKindly refer to the above table and type the Sr.No. of the Appliance you would like to buy: "))
        print("\n")
        if x==1:
            print(table2)
            a=int(input("\nKindly refer to the above table and type the Sr.No. of the Model of Washing Machine you would like to buy: "))
        elif x==2:
            print(table3)
            b=int(input("\nKindly refer to the above table and type the Sr.No. of the Model of Microwave Oven you would like to buy: "))
        elif x==3:
            print(table4)
            ac=int(input("\nKindly refer to the above table and type the Sr.No. of the Model of Air Conditioner you would like to buy: "))
        elif x==4:
            print(table5)
            d=int(input("\nKindly refer to the above table and type the Sr.No. of the Model of Chimney you would like to buy: "))
        elif x==5:
            print(table6)
            e=int(input("\nKindly refer to the above table and type the Sr.No. of the Model of Refrigirator you would like to buy: "))
        else:
            print("\nInvalid input")
            inp()

    x=int(input("\nKindly refer to the above table and type the Sr.No. of the Appliance you would like to buy: "))
    print("\n")
    if x==1:
        print(table2)
        a=int(input("\nKindly refer to the above table and type the Sr.No. of the Model of Washing Machine you would like to buy: "))
    elif x==2:
        print(table3)
        b=int(input("\nKindly refer to the above table and type the Sr.No. of the Model of Oven you would like to buy: "))
    elif x==3:
        print(table4)
        ac=int(input("\nKindly refer to the above table and type the Sr.No. of the Model of AC you would like to buy: "))
    elif x==4:
        print(table5)
        d=int(input("\nKindly refer to the above table and type the Sr.No. of the Model of Chimney you would like to buy: "))
    elif x==5:
        print(table6)
        e=int(input("\nKindly refer to the above table and type the Sr.No. of the Model of Refrigirator you would like to buy: "))
    else:
        print("\nInvalid input")
        inp()
                
    n=int(input('\nEnter the quantity of product you want: '))
    name=input('\nYour Name: ')
    mobile=input('\nYour Mobile No.: ')
    
    address=''
    total=0
    u=0
    i=0
    ch=0
    che=0
    
    j=input("\nDo you want the product to be delivered at a given address @INR 300? Enter Y/N: ")
    
    if j=='Y' or j=='y':
        u=300
        total=total+u
    elif j=='N' or j=='n':
        u=0
        
    k=input("\nDo you want the product to be installed after delivery @INR 500 ? Enter Y/N: ")
    
    if k=='Y' or k=='y':
        i=500
        total=total+500
    elif k=='N' or k=='n':
        i=0
    if k=='Y' or k=='y' or j=='Y' or j=='y':
        address=input('\nYour Address: ')
                
    print('\nHere are the modes of payment we accept: ')
    print('1. Cash on Delivery')
    print('2. Credit/Debit Card')
    z=int(input('Please Select 1 or 2: '))
    if z==2:
            card=int(input("\nEnter card no.: "))
            cvv=int(input("\nEnter CVV: "))

    print('\nHere is the bill of your order:')
    if x==1:
        selectwash=("""select sale_price from washing_machines where SrNo = %s""")
        c.execute(selectwash,(a,))
        washprice=c.fetchall()
        for washprice1 in washprice:
            washprice2=washprice1[0]
            print("\nPrice per Unit: ", washprice2)
        total=total+washprice2*n
                
    elif x==2:
        selectmicro=("""select sale_price from microwave_ovens where SrNo = %s""")
        c.execute(selectmicro,(b,))
        microprice=c.fetchall()
        for microprice1 in microprice:
            microprice2=microprice1[0]
            print("\nPrice per Unit: ", microprice2)
        total=total+microprice2*n
                        
    elif x==3:
        selectac=("""select sale_price from air_conditioners where SrNo = %s""")
        c.execute(selectac,(ac,))
        acprice=c.fetchall()
        for acprice1 in acprice:
            acprice2=acprice1[0]
            print("\nPrice per Unit: ", acprice2)
        total=total+acprice2*n
            
    elif x==4:
        selectchim=("""select sale_price from chimneys where SrNo = %s""")
        c.execute(selectchim,(d,))
        chimprice=c.fetchall()
        for chimprice1 in chimprice:
            chimprice2=chimprice1[0]
            print("\nPrice per Unit: ", chimprice2)
        total=total+chimprice2*n
            
    elif x==5:
        selectfridge=("""select sale_price from refrigerators where SrNo = %s""")
        c.execute(selectfridge,(e,))
        fridgeprice=c.fetchall()
        for fridgeprice1 in fridgeprice:
            fridgeprice2=fridgeprice1[0]
            print("\nPrice per Unit: ", fridgeprice2)
        total=total+fridgeprice2*n

    print("No. of items: ",n)
    if u!=0 and i==0:
        print("Delivery Charges: ",u)
    elif i!=0 and u==0:
        print("Installation Charges: ",i)
    elif i!=0 and u!=0:
        print("Delivery Charges: ",u)
        print("Installation Charges: ",i)
    print("\nFINAL TOTAL: ",total,"\n")
    if z==1:
        print("Mode of Payment: Cash on Delivery")
    elif z==2:
        print("Mode of Payment: Credit/Debit Card")
        print("Card No.: ",card)
            
    print("\nCustomer Name:",name)
    print("Mobile No.: ",mobile)
    if address != '':
        print("Address: ",address)

    print("\nPlease read the Bill Carefully.")
    print("1. Confirm Payment")
    print("2. Cancel the Above Order")
    concan=int(input("Please Select 1 or 2: "))
    print("\n")
    if concan == 1:
        print("\nYour order has been confirmed. Thank you for shopping with us.")
        complete='y'
    elif concan == 2:
        print("Previous order has been Canceled")
        print("1. Order a different Product")
        print("2. Exit")
        orex=int(input("Please Select 1 or 2: "))
        if orex==2:
            exit()
        
