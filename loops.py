#!/usr/bin/python3

def main():
    #get a number from the user
    num = int(input("Type in a number: "))
    a, result = 0 , 0
    #loop through all the numbers between 1 and num
    while a <= num:
    #if number is odd add to results
      if a % 2 == 1:
        print(a)
        result += a
      a += 1
    #print result
    print(result)
if __name__ == "__main__": main()