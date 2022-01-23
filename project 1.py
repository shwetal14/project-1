#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#               Food Ordering app for a restaurant.


class Restro:
def def_default:
self.food = {1: "tandoori chicken", 2: "vegan burger", 3: "truffle cake" , 4: "noodles", 5: "pastry"}
self.food_items_id = len(self.food)+1
self.ordered_items = []
self.personal_items = {}



  #  Admin Functionalities
  
 def food_items(self):
    self.name = input("Enter the food name:")
    self.quantity = int(input("Enter the quantity:"))
    self.price = float(input("Enter the price:"))
    self.stock = int(input("Enter the stock in kg:")
    self.discount = int(input("Enter the discount value:"))
    self.item = {"name":self.name, "quantity":self.quantity, "price :self.price, "discount:self.discount"}
    self.food_items_id = len(self.food)+1
    self.food[self.food_id] = self.item
print("Item added successfully \n", self.food)
               
               
               def remove_items(self):
print("surely you want to delete item")
    del self.food[int(input("Enter the food id you want to delete:''))]
print("Item is deleted successfully")
print("Remaining food items are", self.food)
                        
                        
def edit_food_items(self):
 f_id = int(input("Enter the food_id you want to update:"))
                        
    # {"1:  tandoori chicken , 2: vegan burger , 3: truffle cake , 4: noodles , 5: pastry"}
    for i in self.food[f_id]:
      self.food[f_id] = input("Enter the" +i+ " You want to update:")
                        print("food item is updated successfully\n", self.food)
                        
                        def all_food_items(self):
                             print("list of all food items are:")
                        for i in self.food:
                            print("food id : ", i ,"\n")
                        for j in self.food[i]:
                            print(j,":",self.food[i][j])
                        
                        
   # User Functionalities
                        
        def register(self):
                        
self.fullname = input("Enter your full name")
self.phonenumber = int(input("Enter 10 digit phone no"))
self.email = input("Enter your mail")
self.address = input("Enter your full address")
self.username = input("Choose your username")
self.password = input("Choose your password")
self.personal_details : {"self.name" : self.name , "phone number" : self.phonenumber , "email" : self.email , "address" : self.address , "self.username" : username , "self.password" : password}

 if password ! = confirm_password:
print("Password dont match! ! ! !")
                        
 else:
    if len(password) < = 6:
    print("Password is too short.......Please Choose Strong Password") 
       
                        
    else:
        print("Congrats.....! ! ! Your Account created successfully")                
                        
    
                        
                        
        def login(self):
         while true:
       user_id = input("Enter your user_id")
                        password = input("Enter your password")
                        if user_id == self.username:
                        if password == self.password:
                        print("Congrats you have successfully login")
                        break
                        else:
                        print("Incorrect details")
                        else:
                        print("Incorrect details")
                        
                        
    def place_food_items(self): 
        list_of_fooditems = {1:{"name" : tandoori chicken, "quantity" : 4 pieces ,"prices" : INR 240},
                             2:{"name" : vegan burger, "quantity" : 1 piece ,"prices" : INR 320},                                                                          
                             3:{"name" : truffle cake, "quantity" : 500gm ,"prices" : INR 900}                                                               
                             4:{"name" : noodles, "quantity" : 2 plates , "prices" : INR 200}
                             5:{"name" : Pastry, "quantity" : 5 pieces , "prices" : INR 500}}
                         
                        print("Menu list")
                            user_input = int(input("select food item you need to place"))
                        if user_input == 1:
                            self.ordered_items.append()
                        if user_input == 2:
                        else:
                             print("choose from the Menu")
                        def order_history(self):
                        for i in ordered_item:
                            print(i)
        
                        
                    
                        
            

