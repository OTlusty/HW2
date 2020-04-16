#Skeleton file for HW2 - Spring 2020 - extended intro to CS

#Add your implementation to this file

#you may NOT change the signature of the existing functions.

#Change the name of the file to include your ID number (hw2_ID.py).


############
# QUESTION 1
############

# 1a

import time # delete

def sum_divisors(n): # if n = 1 what will be returned? 
    """
    Insert a natural number > 0 to get the sum of its
    absolute divisors (divisors < number) 
    
    """
    number = n
    assert (type(number) == int) and (number > 0) ## is necessary? 
    
    if number == 1: # 1 is not absolute divided by 1 
        result = 0
        return result

    result = 1 # number > 1 can be absolute divivded by 1 
    for divisor in range(2, int((number)**0.5 + 1)):
        if number % divisor == 0: 
            if (number // divisor) == divisor: # Abstention of adding the same divisor twice 
                result += divisor
            else:
                result += (divisor + (number // divisor))
    
    return result
    

# 1b
def legal_par(st):
    """
    Insert a string with signs contain in [,],{,},(,),<,>
    The function will check two conditions:
    1. if there is a match for every sigh - for examle "[" and "]"
    2. if the first sigh to the left for every closer sigh is the match opner - for example "[]" 

    if so - True, else - False    
    
    """
    result = False
    
    string = st 
    string_len = len(string) 
    sighs_lst = ['[','{','(','<',']','}',')','>']
    cnt_lst = []    
    stack_of_open_lst = [] 
    
    for closer in sighs_lst:  
        cnt_closer = string.count(closer)
        cnt_lst.append(cnt_closer) 
    
    if not((cnt_lst[0] == cnt_lst[4]) and (cnt_lst[1] == cnt_lst[5]) # count of match closer pairs isn't equal
        and (cnt_lst[2] == cnt_lst[6]) and (cnt_lst[3] == cnt_lst[7])):
        return result # False

    if string_len == 0: ## what to do for empty? 
        result = True
        return result
    
    for sign in range(string_len):
        if string[sign] in sighs_lst[:4]:               # if opener add to stack 
            stack_of_open_lst.append(string[sign])
        elif len(stack_of_open_lst) == 0:               # sign is a closer but the stack is empty 
            return result # False 
        else:                                           # must be closer and stack isn't empty 
            sign_closer_index = sighs_lst.index(string[sign])
            last_opener = stack_of_open_lst.pop()
            last_opener_index = sighs_lst.index(last_opener)
            if not(last_opener_index + 4 == sign_closer_index): # check to opener match the closer sign 
                return result # False

    result = True
    return result 
    
# 1c
def spiral_sum(k):
    """
    for a given odd natural number the function will calculate the summary of the digits on the matrix oblique.
    the matrix which calculated is built by statring from the center and writing natural number (starting with 1) clockwise

    explaination for sum_k:
    for every step we add to result only the new corners which conveniently can easely calculated.
    we take the right upper corner (k^2), add the right lower corner (k^2 - 3*(k-1)) and multiply by 2 (for the two
    left corners), than rearrange it and get sum_k = 4k^2 -6k+6
    we don't want to add the center of the matrix (k = 1) twice so we will start with result = 1.
    
    check it yourself and see it fit :) 

    p.s. the function spiral_sum doesn't built the matrix itself. 
    
    """

    result = 1
    
    for number in range(3,k+1,2):
        sum_k = 4*number*number-6*number+6
        result += sum_k

    return result

############
# QUESTION 2
############

# 2b
def power_new(a,b):
    """ computes a**b using iterated squaring """
    
    result = 1
    
    b_bin = bin(b)[2:]
    reverse_b_bin = b_bin[: :-1]
    for bit in reverse_b_bin: 
        if bit == "1":
            result = result*a
        a = a*a 
    return result

# 2c
def modpower_new(a, b, c):
    """ computes a**b mod c using iterated squaring
        assumes b is nonnegative integer  """

    result = 1 # a**0
    
    while b > 0:
        if b % 3 == 0:
            result = (result) % c
            a = (a*a*a) % c
        if b % 3 == 1:
            result = (result*a) % c 
            a = (a*a*a) % c
        if b % 3 == 2:
            result = (result*a*a) % c
            a = (a*a*a) % c 
        b = b // 3
    return result


############
# QUESTION 3
############

# 3a
def inc(binary): 
    """ Calculate adiition of 1 to a binary string. """

    result = ""
    
    carry = "1" # we want to add 1 to the first bit 
    binary_reversed = binary[::-1]
    LEN_BINARY = len(binary)

    for bit in range(LEN_BINARY):
        sum_bit = binary_reversed[bit] + carry
        if sum_bit == "11": # case: 1 + 1
            result = "0" + result
            carry = "1"
        elif (sum_bit == "10") or (sum_bit == "01"): # case 1+0 or 0+1
            result = "1" + result
            carry = "0"
        else: # case 0+0
            result = "0" + result
            carry = "0"

    if carry == "1": # case: remaining carry at the end 
        result = "1" + result
    return result    

# 3b
def dec(binary):
    """
    Binary subtraction by 1 to a binary string.
    Positive numbers only (as input and/or output).

    """

    result = ""
    
    binary_reversed = binary[::-1]
    LEN_BINARY = len(binary)

    if binary_reversed[0] == "1": 
            result = binary[:-1] + "0"
            return result

    for bit in range(LEN_BINARY): 
        if binary_reversed[bit] == "1":
            count_bits_left_to_the_one_bit = LEN_BINARY - (bit + 1) # count the number of bit unchange
            result = binary[:count_bits_left_to_the_one_bit] + "0" + "1" * bit            
            if result[0] == "0":
                result = result[1:]
                return result
            return result
    
# 3c
def sub(bin1, bin2): 
    """
    Binary subtraction - subtract bin2 from bin1.
    Positive numbers only (as input and/or output).
    
    """
    result = ""
    
    bin1_reversed = bin1[::-1]
    bin2_reversed = bin2[::-1]
    LEN_BIN2 = len(bin2) 
    
    for bit in range(LEN_BIN2):
        if bin2_reversed[bit] == "0": # x - 0 = x
            result = bin1[-1] + result 
        else:
            bin1 = dec(bin1)
            result = bin1[-1] + result
        bin1 = bin1[:-1] 

    result = bin1 + result
    for result_bit in result:
        if (result_bit == "0") and (len(result) > 1):
            result = result[1:]
        else:
            return result

# 3d
def leq(bin1, bin2): # True if bin1 <= bin2 
    """ Leq check if bin1 <= bin2 """

    result = True
    
    LEN_BIN1 = len(bin1)
    LEN_BIN2 = len(bin2)

    if LEN_BIN1 < LEN_BIN2:
        return result # True 
    elif LEN_BIN1 > LEN_BIN2:
        result = False
        return result

    # LEN_BIN1 = LEN_BIN2
    for bit in range(LEN_BIN1):
        if bin1[bit] < bin2[bit]:
            return result # True 
        elif bin1[bit] > bin2[bit]:
            result = False
            return result

    # bin1 == bin2
    return result # True
    
# 3e
def div(bin1, bin2): ## bin1 // bin2 
    """ Div calculate bin1 // bin2 in binary """

    result = "" 
    
    if bin1 == bin2:
        result = "1"
        return result 
    elif leq(bin1, bin2): # (bin1 < bin2) and (bin1 != bin2)
        result = "0"
        return result

    ## bin1 > bin2
    count = "0"
    while leq(bin2, bin1): # is still bin2 <= bin1? 
        bin1 = sub(bin1, bin2) # bin1 = bin1 - bin2 
        count = inc(count) # count += 1 in binary
        
    result = count
    return result
    
############
# QUESTION 4
############

# 4a
def has_repeat1(s, k): 
    """
    Check if there is a repeatition of k signs
    in the string s.
    s isn't empty and 0 < k <= lenth of s 
    
    """
    result = False
    string = s 
    
    LEN_STRING = len(string) 
    LEN_OF_REPEATION = k 
    repeation_lst = [] 

    NUMBER_OF_SUBSTRINGS = LEN_STRING - LEN_OF_REPEATION + 1 
    
    for sign in range(NUMBER_OF_SUBSTRINGS):
        repeat = string[sign:sign + LEN_OF_REPEATION] 
        if repeat in repeation_lst:
            result = True
            return result
        else:
            repeation_lst.append(repeat)

    return result # False

# 4b
def has_repeat2(s, k):
    """
    Check if there is a repeatition of k signs
    in the string s.
    s isn't empty and 0 < k <= length of s
    
    """
     
    result = False
    string = s 
    
    LEN_STRING = len(string)
    LEN_OF_REPEATION = k 

    NUMBER_OF_SUBSTRINGS = LEN_STRING - LEN_OF_REPEATION + 1
    
    for sign in range(NUMBER_OF_SUBSTRINGS):
        repeat = string[sign:sign + LEN_OF_REPEATION]

        sliced_string = string[sign + 1:]
        LEN_OF_SLICED_STRING = len(sliced_string) 
        NUMBER_OF_SUB_SUBSTRING = LEN_OF_SLICED_STRING - LEN_OF_REPEATION + 1
        
        for sub_string in range(NUMBER_OF_SUB_SUBSTRING): 
            check_repeatition = sliced_string[sub_string:sub_string + LEN_OF_REPEATION]
            if repeat == check_repeatition:
                result = True
                return result
            
    return result # False
    
############
# QUESTION 5
############

def reading(n): 
    """
    input must be an integer bigger than 0 and get R(n). 
    
    Define a function R:N+ --> {'0', '1', ... '9'}
    1. R(1) = "1"
    2. R(n>1) = R(n-1) when you "read" the digits from left to right if we encounter
        a equence of the same digit we will write first the length of the sequence and than the digit itself.

    examples: R(2) = "11", R(3) = "21", R(4) = "1211"...

    The function finds R(n) by calculating the lower organs (R(2).. R(n-1))
    
    """

    ## set the paramters for first iteration 
    result = ""
    organ_number = n 
    current_organ = "1" # R_1 = "1"
    new_organ = "" 

    for organ_number in range(2, organ_number + 1): # find R_2 --> R_n
        len_of_current_organ = len(current_organ) 
        count_sign = 1 

        for sign in range(len_of_current_organ): 
            if sign != 0: 
                if current_organ[sign] == current_organ[sign - 1]: # another sign in a raw 
                    count_sign += 1
                else:
                    new_organ = new_organ + str(count_sign)+ current_organ[sign - 1]
                    count_sign = 1 

        ## the last set of signs haven't been added to new_organ yet.
        ## last set of signs are allways "1"s or a single "1"
        new_organ = new_organ + str(count_sign)+ "1" 
        
        ## new_organ found, set the paramters for the next iteration 
        current_organ = new_organ 
        new_organ = ""
    
    result = current_organ
    return result 
    
############
# QUESTION 6
############
def max_div_seq(n, k): ## ("33456789", 3)
    """
    Count the longest sequence of digits in an natural number (n) divided by k.

    """
    
    result = 0

    string_number = str(n)
    LEN_OF_STRING_NUMBER = len(string_number) 
    divider = k 

    count_lst = [0]
    count = 0 
    for sign in range(LEN_OF_STRING_NUMBER):
        if int(string_number[sign]) % divider == 0:
            count += 1
        elif count != 0: 
            count_lst.append(count) 
            count = 0

    if count != 0: # last countdown haven't add yet
        count_lst.append(count) 
    
    max_count = max(count_lst)
    result = max_count
    return max_count

########
# Tester
########

def test():
    if sum_divisors(4) != 3 or \
       sum_divisors(220) != 284:
        print("error in sum_divisors")
        
    if not legal_par("<<>>") or legal_par("<{>}"):
        print("error in legal_par")
    if not legal_par("<<{}<>()[<>]>>") or legal_par("{{{]}}"):
        print("error in legal_par")

    if spiral_sum(3) != 25 or spiral_sum(5) != 101:
        print("error in spiral_sum")
        
    if power_new(2,3) != 8:
        print("error in power_new()")

    if modpower_new(3, 4, 5) != pow(3, 4, 5) or \
       modpower_new(5, 4, 2) != pow(5, 4, 2):
        print("error in modpower_new()")
    
    if inc("0") != "1" or \
       inc("1") != "10" or \
       inc("101") != "110" or \
       inc("111") != "1000" or \
       inc(inc("111")) != "1001":
        print("error in inc()")

    if dec("1") != "0" or \
       dec("10") != "1" or \
       dec("110") != "101" or \
       dec("1000") != "111" or \
       dec(dec("1001")) != "111":
        print("error in dec()")
        
    if sub("0", "0") != "0" or \
       sub("1000", "0") != "1000" or \
       sub("1000", "1000") != "0" or \
       sub("1000", "1") != "111" or \
       sub("101", "100") != "1":
        print("error in sub()")

    if leq("100","11") or not leq("11", "100"):
        print("error in leq")
    if div("1010","10") != "101" or div("11001", "100") != "110":
        print("error in div")
        
    if not has_repeat1("ababa", 3) or \
       has_repeat1("ababa", 4) or \
       not has_repeat1("aba",1):
        print("error in has_repeat1()")

    if not has_repeat2("ababa", 3) or \
       has_repeat2("ababa", 4) or \
       not has_repeat2("aba",1):
        print("error in has_repeat2()")
                
    if [reading(i) for i in range(1, 6)] != ['1', '11', '21', '1211', '111221']:
        print("error in reading")

    if max_div_seq(23300247524689, 2) != 4:
        print("error in max_div_seq()")
    if max_div_seq(1357, 2) != 0:
        print("error in max_div_seq()")        
