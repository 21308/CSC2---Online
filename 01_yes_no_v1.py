# Functions go here... 
def yes_no (question):
    valid = False 
    while not valid:
      response = input (question) .lower ()

      if response == "yes" or response == "y":
        response = "yes"
        valid = True
        
      elif response == "no" or response == "n":
        response = "no" 
        valid = True

      else: 
          print ("Please answer yes / no")
    return response








# Main routine goes here...
show_instructions = yes_no ("Do you want to "
                            "read the instructions?")
print (("You chose {}").format(show_instructions))