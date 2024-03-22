# Functions go here... 
def yes_no (question):
    valid = False 
    while not valid:
      response = input (question) .lower ()

      if response == "yes" or response == "y":
        response = "yes"
        valid = True
        
      elif response == "no" or response == "n":
        print("We are done ")
        valid=True

      else: 
          print ("Please answer yes / no")
    return response








# Main routine goes here...
show_instructions = yes_no ("Do you want to "
                            "read the instructions? ")
if show_instructions=="yes":
  print (("Instructions go here "))