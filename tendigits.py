
# Find a ten digits integer with all ten digits, 
# such that the first n digits (1<n<10) are divisible by n. 
# The integer should thus contain all 10 different symbols 1,2,3,4,5,6,7,8,9,0.

# recursive function that should in theory print all of the possible answers
def get_nums(num):
    if len(num) < 9:
            for i in range(1, 10):
                # checks if current number plus new digit i fits the constraints
                if int(num + str(i)) % (len(num) + 1) == 0 and str(i) not in num:
                    get_nums(num + str(i))
            return 
    else:
        print(num + "0") #last digit must be a zero
        return

get_nums("")

    
    

