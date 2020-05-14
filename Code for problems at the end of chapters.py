# PSET1: Problem 1
#s = 'azcbobobegghakl'
#count = 0
#for i in range(len(s)):
#    if s[i] in 'aeiou':
#        count+=1
#print("Number of vowels: " + str(count))

# PSET1: Problem 2
#s = 'azcbobobegghakl'
#o = 'bob'
#count=0
#for i in range(len(s)):
#    if i < len(s)-2: #need this as otherwise i+3 becomes "index out of range"
#        if s[i:i+3] == o:
#            count+=1
#print("Number of times bob occurs is: "+str(count))

# PSET1: Problem 3
## wrong solution - this one checks for whether substring is alphabetical, not alphabetical order
#s = 'azcbobobegghakl'
#
## part 1 - generate an array of all possible sequences and order it
#found_s_array = []
#for start_index in range(len(s)):
#    length = len(s)
#    for end_index in range(length, 0, -1):
#        found_s = s[start_index:end_index]
#        if len(found_s) > 0:
#            found_s_array.append(found_s)
#found_s_array.sort(key = len, reverse=True)
#
## part 2 - check which ones are present 
#alphabet = 'abcdefghijklmnopqrstuvwxyz'
#for s in found_s_array:
#    if s in alphabet:
#        print(s)
#        break


# right solution
#s = 'azcbobobegghakl'
#alphabet = 'abcdefghijklmnopqrstuvwxyz'
#
## step 1 - convert to numbers
#r_dict = {i : alphabet[i] for i in range(len(alphabet))}    
#a_dict = {alphabet[i] : i for i in range(len(alphabet))}    
#
#def convert_to_num(string):
#    num_array = []
#    for i in string:
#        num_array.append(a_dict[i])
#    return num_array
#
#num_s = convert_to_num(s)
#num_a = convert_to_num(alphabet)
#
## step 2 - create array
#found_s_array = []
#for i in range(len(num_s)):
#    i_array = []
#    i_array.append(num_s[i])
#    for j in range(len(num_s)):
#        if j > i:
#            if num_s[j] >= num_s[j-1]:
#                i_array.append(num_s[j])
#            else:
#                break
#    found_s_array.append(i_array)
#    
## step 3 select largest element and convert to string
#result_num = max(found_s_array, key=len)
#result = ""
#for i in result_num:
#    letter = r_dict[i]
#    result+=str(letter)
#
#print(result)


# best solution posted on forums
#s = 'azcbobobegghakl'
#prev = ' '
#start = size = l_start = l_size = 0
# start and size are live counters; start = almost like a pointer where the loop should go; size = how big is the current array
# l_start and l_size are "largest" trackers
#for c in s:
#    if c >= prev:
#        size += 1
#        print(start,size,l_start,l_size)
#    else:
#        if size > l_size:
#            l_size = size
#            l_start = start
#        start += size
#        size = 1
#    prev = c
#if size > l_size:
#    l_size = size
#    l_start = start
#print('Longest substring in alphabetical order is:', s[l_start: l_size+l_start])

# chapter 3 simple algos
# https://courses.edx.org/courses/course-v1:MITx+6.00.1x+2T2019a/courseware/0de4fecc5a9a4749923133fcf4de181f/62f08cc899344863a1ab678aee506dec/?child=first

#num = 59
#low = 0
#high = 100
#
## ITERATIVE VERSION
#guess = int((high-low)/2) #first guess outside of the loop
#while guess != num: #keep checking
##    print('wrong guess: '+str(guess))
#    if guess > num: #bucket
#        high = guess
#    elif guess < num:
#        low = guess
#    guess = int((high-low)/2+low) #update the guess
##print(guess)
#
## RECURSIVE VERSION
#def guesser(num, low, high):
#    guess = int((high-low)/2)+low
#    if guess == num:
#        return guess
#    elif guess < num:
#        return guesser(num, guess, high)
#    elif guess > num:
#        return guesser(num, low, guess)
#
#print(guesser(59,0,100))

# now with user input
#low = 0
#high = 100
#guess = int((high-low)/2)
#
#print('Please think of a number between 0 and 100!')
#
#print('Is your secret number ' + str(guess) + '?')
#print('Enter \'h\' to indicate the guess is too high. Enter \'l\' to indicate the guess is too low. Enter \'c\' to indicate I guessed correctly.', end = ' ')
#user_input = input()
#if user_input not in ('clh'):
#    print('Sorry, I did not understand your input.')
#    print('Is your secret number ' + str(guess) + '?')
#    print('Enter \'h\' to indicate the guess is too high. Enter \'l\' to indicate the guess is too low. Enter \'c\' to indicate I guessed correctly.', end = ' ')
#    user_input = input()
#
#while user_input != 'c':
#    if user_input =='h':
#        high = guess
#    elif user_input =='l':
#        low = guess
#    guess = int((high-low)/2+low)
#    
#    print('Is your secret number ' + str(guess) + '?')
#    print('Enter \'h\' to indicate the guess is too high. Enter \'l\' to indicate the guess is too low. Enter \'c\' to indicate I guessed correctly.', end = ' ')
#    user_input = input()
#    if user_input not in ('clh'):
#        print('Sorry, I did not understand your input.')
#        print('Is your secret number ' + str(guess) + '?')
#        print('Enter \'h\' to indicate the guess is too high. Enter \'l\' to indicate the guess is too low. Enter \'c\' to indicate I guessed correctly.', end = ' ')
#        user_input = input()
#print('Game over. Your secret number was: ' + str(guess))


#bisection search for a character inside a string:

#normal, NON RECURSIVE VERSION
#def isIn(char, aStr):
#    '''
#    char: a single character
#    aStr: an alphabetized string
#    
#    returns: True if char is in aStr; False otherwise
#    '''
#    # Your code here
#    aStr = ''.join(sorted(aStr.lower()))
#
#    first = 0
#    last = len(aStr)-1
#    guess = (last-first)//2
##    print('just tried ', aStr, first, last, guess)
#    
#    while aStr[guess] != char:
#        if aStr[guess] < char:
#            first = guess
#            guess = (last-first)//2+first+1
#        elif aStr[guess] > char:
#            last = guess
#            guess = (last-first)//2
##        print('just tried ', aStr, first, last, guess)
#    print('guessed! '+aStr[guess], guess)
#    
#c = 'a'
#s = 'abcde'
#isIn(c,s)

# recursive version 1
#aStr = 'abcde'
#char = 'e'
#aStr = ''.join(sorted(aStr.lower()))
#first = 0
#last = len(aStr)-1
#guess = (last-first)//2
#def func(first, last, guess, char):
#    if aStr[guess] == char:
#        print('guessed! '+aStr[guess], guess)
#    elif aStr[guess] < char:
#        func(first=guess, last=last, guess=(last-first)//2+first+1, char=char)
#    else:
#        func(first=first, last=guess, guess = (last-first)//2, char=char)
#func(first, last, guess, char)


# recursive version 2
#def isIn(char, aStr):
#    aStr = ''.join(sorted(aStr.lower()))
#    first = 0
#    last = len(aStr)
#    guess = (last-first)//2
#
#    # this basically checks for failure and prevents over-running
#    if len(aStr) <= 1 and aStr != char: #important to have <= not ==
#        return False
#
#    if aStr[guess] == char:
#        return True    
#    elif char > aStr[guess]:
#        return isIn(char, aStr[guess:]) #really fucking important - add "return" here!!!!
#    elif char < aStr[guess]:
#        return isIn(char, aStr[:guess])
#        
#x = isIn('e','aadfadsfasbc')
#print(x)

#week2 extra problem1
#import math
#def polysum(n, s):
#    P = n*s
#    S = (0.25*n*s**2)/math.tan(math.pi/n)
#    return float("{0:.4f}".format(S+P**2))
#
#print(polysum(4, 2))
#
##PSET2: Problem 1
#balance = 42
#annualInterestRate = 0.2
#monthlyPaymentRate = 0.04
#
#for i in range(12):
#    ub = balance - balance * monthlyPaymentRate
#    ir = annualInterestRate/12
#    balance = ub + ir*ub
#print('Remaining balance: ' + "{0:.2f}".format(balance))

#PSET2: Problem 2
#balance = 4773
#annualInterestRate = 0.2
#
#x = 10
#b = balance
#while b > 0:
#    b = balance
#    for i in range(12):
#        b = (b - x) * (1 + annualInterestRate/12)
#    x+=10
#else:
#    x-=10
#
#print('Lowest Payment: ' +str(x))

#PSET2: Problem 3

# iterative version
#starting_balance = 4773
#annualInterestRate = 0.2
#
#def calc_balance(balance, guess):
#    for i in range(12):
#        balance = (balance - guess) * (1 + annualInterestRate/12)
#    return balance
#
#balance = starting_balance #one off 
#
#lower_b = balance/12
#upper_b = balance*(1+annualInterestRate/12)**12/12
#guess = (upper_b-lower_b)/2+lower_b
#balance = calc_balance(starting_balance, guess)
#print('balance is '+"{0:.4f}".format(balance) +' with guess of ' + "{0:.4f}".format(guess))
#
#while round(balance,2) != 0:
#    if balance > 0:
#        print('pay MORE!! ')
#        lower_b = guess
#    elif balance < 0:
#        print('too much!')
#        upper_b = guess
#    guess = (upper_b-lower_b)/2+lower_b
#    balance = calc_balance(starting_balance, guess)
#    print('balance is '+"{0:.4f}".format(balance) +' with guess of ' + "{0:.4f}".format(guess))
#
#print('DDDDDDdone!!! ' +str(guess))

# recursive version
# these need to be happenign outside of the function, otherwise if you try to include balance as argument it gets redefined with every loop and that fucks the calc
#starting_balance = 4773
#annualInterestRate = 0.2
#lower_b = starting_balance/12
#upper_b = starting_balance*(1+annualInterestRate/12)**12/12
#
#def calc_balance(balance, guess):
#    for i in range(12): balance = (balance - guess) * (1 + annualInterestRate/12)
#    return balance
#
#def find_payment(lower_b, upper_b): #the big revelation I had here was not to pass in balance itself, because then it gets updated on every recursive turn, and we actually don't want that (formula for balance calc requires startning balance every time)
#
#    guess = (upper_b-lower_b)/2+lower_b
#    balance = calc_balance(starting_balance, guess)
#    print('balance is '+"{0:.4f}".format(balance) +' with guess of ' + "{0:.4f}".format(guess))
#
#    if round(balance,1) == 0:
#        print('DDDDDDdone!!! ' +str(guess))
#        return guess
#    elif balance > 0:
#        print('pay MORE!! ')
#        return find_payment(guess, upper_b)
#    elif balance < 0:
#        print('too much!')
#        return find_payment(lower_b, guess)
#        
#find_payment(lower_b, upper_b)


# end of chapter 5 problem on primes
#def genPrimes():
#    primes = []
#    for i in range(0,20):
#        if i == 1 or i == 0:
#            continue
#        else:
#            for p in primes:
#                if i % p == 0:
#                    break
#            else:
#                primes.append(i)
#    return primes
#
#def genPrimes():
#    primes = []
#    for i in range(0,20):
#        if i == 1 or i == 0:
#            continue
#        else:
#            for p in primes:
#                if i % p == 0:
#                    break
#            else:
#                next = i
#                yield i
#                primes.append(i)
##    return primes
#
#x = genPrimes()
#print(x.__next__())
#print(x.__next__())
#print(x.__next__())
#print(x.__next__())
#        