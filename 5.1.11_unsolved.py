
#The Fibonacci sequence is a number sequence where each
#number is the sum of the previous two numbers. The first
#two numbers are defined as 0 and 1, so the third number is
#1 (0 + 1 = 1), the fourth number is 2 (1 + 1 = 2), the
#fifth number is 3 (1 + 2 = 3), the sixth number is 5
#(2 + 3 = 5), and so on.
#
#Below we've started a class called FibSeq. At any time,
#FibSeq holds two values from the Fibonacci sequence:
#back1 and back2.
#
#Create a new method inside FibSeq called next_number. The
#next_number method should:
#
# - Calculate and return the next number in the sequence,
#   based on the previous 2.
# - Update back2 with the former value of back1, and update
#   back1 with the new next item in the sequence.
#
#This means that consecutive calls to next_number should
#yield each consecutive number from the Fibonacci sequence.
#Calling next_number 5 times would print 1, 2, 3, 5, and 8.


class FibSeq:
    def __init__(self):
        self.back1 = 1
        self.back2 = 0
 #       self.counter = 0
    
    def next_number(self):
#        self.next_number = self.back1 + 1
#        returns Fibonacci of x""”
 #       x = self.back1
#        print
        
 #       newfib.back1 = newfib.back1 - 1
 #       back2 = 
        print(newFib.back2)
        if newFib.back2 == 0:
            return 1
        else:
  #          print(newFib.back1 + newFib.back2)
            return newFib.back1 + (newFib.back2)
#        self.age = newage
        var = 5
        var2 = 6
        self.back2 = var
        self.back1 = var2
  #      print(self.back1)

#The code below will test your method. It's not used for
#grading, so feel free to change it. As written, it should
#print 1, 2, 3, 5, and 8.
newFib = FibSeq()
print(newFib.next_number())
print(newFib.next_number())
print(newFib.next_number())
print(newFib.next_number())
print(newFib.next_number())


