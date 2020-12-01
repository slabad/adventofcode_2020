# Open file    
fileHandler = open ("input.txt", "r")
lines = fileHandler.readlines()
fileHandler.close()

numbers = [int(i) for i in lines]
target_number = 2020

for i, number in enumerate(numbers[:-1]): 
    complementary = target_number - number
    if complementary in numbers[i+1:]:  
        answer=number*complementary
        print("Complementary Numbers Found: {} and {}".format(number, complementary))
        print("Answer: ", answer)
        break
else:  
    print("No solutions exist")
