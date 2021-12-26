#Write a function called search_for_string() that takes two
#parameters, a list of strings, and a string. This function
#should return a list of all the indices at which the
#string is found within the list.
#
#You may assume that you do not need to search inside the
#items in the list; for examples:
#
#  search_for_string(["bob", "burgers", "tina", "bob"], "bob")
#      -> [0,3]
#  search_for_string(["bob", "burgers", "tina", "bob"], "bae")
#      -> []
#  search_for_string(["bob", "bobby", "bob"])
#      -> [0, 2]
#
#Use a linear search algorithm to achieve this. Do not
#use the list method index.
#
#Recall also that one benefit of Python's general leniency
#with types is that algorithms written for integers easily
#work for strings. In writing search_for_string(), make sure
#it will work on integers as well -- we'll test it on
#both.


#Write your code here!
def search_for_string(a_list, an_item):
    mylist = []
    #Then, we iterate through the list:
    for i in range(len(a_list)):
        
        #If we've found the item, we're done! Go ahead and
        #return this index.
        if a_list[i] == an_item:
            mylist.append(i)
 #           return i
    return(mylist)

    #If we reach the end of the function it means we never
    #returned an index, which means we never found the item
    #and can return False.
    return False


#def search_for_string(mylist, search):
 #   i = 0
 #   ret_list = []
 #   for word in mylist:
 #       print(search in word)
 #       if True:
 #           mylist.append(i)
 #           i = i + 1
#        else:
 #           i = i + 1
#            continue
 #   return(my_list)

#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs
#If your function works correctly, this will originally
#print: [1, 4, 5]
sample_list = ["artichoke", "turnip", "tomato", "potato", "turnip", "turnip", "artichoke"]
print(search_for_string(sample_list, "turnip"))

