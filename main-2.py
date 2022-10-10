#creates the function
def blastoff(c):
  while c > 0:
    print(c) #prints the value being displayed
    c = c -1 #subtracts by 1 until hits zero.
    if c == 0: #inserts a if value for when it reaches 0 to say blastoff
      print("Blastoff!")
      break
    #relays and prints the function
print(blastoff(100))
    

  

