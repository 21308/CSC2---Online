# Functions go here... 
def cash_credit (question):
    valid = False 
    while True:
      response = input (question) .lower ()

      if response == "cash" or response == "ca":
       return "cash"
        
        
      elif response == "credit" or response == "cr":
        return "credit"
        

      else: 
          print ("Please choose a valid payment method")
     

# Main routine goes here...
while True: 
   payment_method = cash_credit("Choose a payment method (cash or credit): ")

   print("You chose", payment_method)

   print(" ")
