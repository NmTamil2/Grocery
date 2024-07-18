

#1.Welcome User

userName = input("Please Enter Your Name : ")
print()
WelcomeMsg = f"Wlecome to NM Store, {userName}"
lenWmsg = len(WelcomeMsg)
print('*'*lenWmsg)
print(WelcomeMsg)
print('*'*lenWmsg)


#2.read data from text file

my_file = open("Available_items.txt")

file_line = my_file.readline()
file_list = my_file.readlines()
##print(file_list)

my_file.close()


#3.Fetch items from list and add to dictionary

items_Avail_dict = {}

print()
print('********** Items Available In Our Store **********')

for item in file_list:
    item_name = item.split()[0]
    item_price = item.split()[1]

    print(f"{item_name}:{item_price}")
    items_Avail_dict.update({item_name : int(item_price)})
print('*'*20)
##print(items_Avail_dict)


#4.Prompt user to add items
print()

shoppingDict = {}

proceedShopping = input("Do you wish to proceed (yes/no): ")
while proceedShopping.lower() == 'yes':
    item_added = input("Add an item: ")
    if item_added.title() in items_Avail_dict:
        item_qty = int(input("Add Quantity : "))
        shoppingDict.update({item_added:{'Quantity':item_qty,'Sub-Total':items_Avail_dict[item_added.title()]*item_qty}})
        print(shoppingDict)
  
    else:
        print("Unable to add unavailable items")
    proceedShopping = input("Do you wish to proceed (yes/no): ")
else:
    print('\n')
    print('***** Bill Summary *****')
    print('\n')
    print('Item   Quantity  Sub-Total')

    total = 0
    for key in shoppingDict:
          print(f"{key}      {shoppingDict[key]['Quantity']}          {shoppingDict[key]['Sub-Total']}")
          total = shoppingDict[key]['Sub-Total']+total
    print(f"Total : {total}")

    print("****** Thank You *****")    
    print("Hope to see you back soon!")
                        
                        
    




