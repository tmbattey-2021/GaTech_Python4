


#This problem uses the same Pet, Owner, and Name classes from
#the previous problem.
#
#In this one, instead of printing a string that lists a single
#pet's owner, you will print a string that lists all of a
#single owner's pets.
#
#Write a function called get_pets_string. get_pets_string should
#have one parameter, an instance of Owner. get_pets_string
#should return a list of that owner's pets according to the
#following format:
#
#David Joyner's pets are: Boggle Joyner, Artemis Joyner

class Name:
    def __init__(self, first, last):
        self.first = first
        self.last = last

class Pet:
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner
        
    def __str__(self):
        i = 0
#        print(len(self.owner.pets))
        while i <  len(self.owner.pets):
  #      return "x = {}".format(self.owner.pets)
            return str(self.owner.pets)
            i = i + 1

        
#    def __repr__(self):
 #       return str(f"{self.owner.pets}")  
        
class Owner:
    def __init__(self, name):
        self.name = name
        self.pets = []
 
#    def __repr__(self):
#        return str(self.pets)
    
    

# {self.label} {self.neighbours}   
 #   def __str__(self):
  #      result = owner.self.pets
  #      + str(self.value) + ', '\
  #      + str(self.weight) + '>'
  #      return result
#Add your get_pets_string function here!

def get_pets_string(owner):
#     def get_owner_string(pet):
 #   pet_first = owner.name.first
 #   pet_last = owner.name.last
    owner_first = owner.name.first
    owner_last = owner.name.last
    pet1 = owner.pets
    print(pet1)
    i = 0
    pet_var = owner.pets[i]
  #  print(pet_var)
 #   print(pet_var.__str__())
    ret_str = " "
    pet_list = []
    while i <  len(owner.pets):
        pet_var = owner.pets[i] 
        pet_list.append(pet_var)
        print(type(pet_var))
        print(pet_var)
     #   ret_str = ret_str + pet_var.__str__()
        i = i + 1
    #    return(pet_var.__str__())
#    pet_first = owner.pets[0]
#    for item in pet_list:
#        print(item)
    return( owner_first.__str__() + " " + owner_last.__str__() + "'s pets are " +".")

    
 #   return(pet_first.__str__() + " " + pet_last.__str__() + "'s owner is " + owner_first.__str__() + " " + owner_last.__str__() + ".")
    
 #   print(owner.name.first)
  #  print(owner.name.last)
#    print(pet_1)
#    return(owner.pets[0].__str__())
 #   print(pets[0])

    
#def get_owner_string(pet):
#    pet_first = pet.name.first
#    pet_last = pet.name.last
 #   owner_first = pet.owner.name.first
 #   owner_last = pet.owner.name.last
 #   return(pet_first.__str__() + " " + pet_last.__str__() + "'s owner is " + owner_first.__str__() + " " + owner_last.__str__() + ".")
    
#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#David Joyner's pets are: Boggle Joyner, Artemis Joyner
#Audrey Hepburn's pets are: Pippin Hepburn
owner_1 = Owner(Name("David", "Joyner"))
owner_2 = Owner(Name("Audrey", "Hepburn"))

pet_1 = Pet(Name("Boggle", "Joyner"), owner_1)
pet_2 = Pet(Name("Artemis", "Joyner"), owner_1)
pet_3 = Pet(Name("Pippin", "Hepburn"), owner_2)

owner_1.pets.append(pet_1)
owner_1.pets.append(pet_2)
owner_2.pets.append(pet_3)

print(get_pets_string(owner_1))
print(get_pets_string(owner_2))