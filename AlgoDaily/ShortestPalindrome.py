# import functools
# import math
# import numpy

# Find Shortest Palindrome Possible
# Word or phrase that reads the same backward as forward

# Need to find the shortest in the word 

# Loop through the word
# For each string starting at that word create a string slice  to match one
# Take the full string -> revserse it and match it the first string
# Check if its a palindrome
# if not go to next loop and decrease second string end length
# as well check full string in reverse

def reverse_string(string):
    return True if string == string[::-1] else False

def shortest_pal(string):
    leng = len(string)
    start = 0
    end = leng - 1

    
    while start < end:
        
        # Does start = end ?
        if string[start] == string[end]:
            temp_string
        
        # Increase start and decrease end
        start += 1
        end -= 1
        

if __name__ == '__main__':
    print("Find Shortest Palindrom Possible")
    pal = 'elbbubble'
    pal2 = 'xmdasdnsadasndsadmx'
    pal3 = 'AVAJAVA'
    
    
    print(reverse_string(pal3))
    print(reverse_string(pal2))
    print(reverse_string(pal))
    
    print(shortest_pal(pal2))