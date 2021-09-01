# Helper Video -> https://www.youtube.com/watch?v=Sx9NNgInc3A&ab_channel=NeetCode

# def wordBreak(s: str, wordDict: [str]) -> bool:
#         pivot_idx = 0
#         matches = 0
#         temp = s
#         for word in wordDict:
#             if word in s[pivot_idx:]:
#                 if s[pivot_idx:].index(word) == 0:
#                     matched_word_len = len(word)
#                     pivot_idx = pivot_idx + matched_word_len
#                     matches += 1
#                 else:
#                     matches -= 1
#                     s = temp

#         return True if ((matches > 1) or (matches == 1 and len(wordDict) == 1 )) else False
            

# print(wordBreak("catsandog", ["cats","dog","sand","and","cat"]))

# # Brute Force Appraoch
# # Check everyone combo of characters in incoming string and check if they are a word in the dict
# # O(n) x (n)

# # First word check len of chars
# # Starting a start of string do those first 4 words equal the word in the string 
# # if so now you know the index and you can start checking for the next work from the end of the last words index in the
# # string O (n * m * n)

# def wordBreak2(s: str, wordDict: [str]) -> bool:

#     piv_idx = 0

#     for word in wordDict:
#         prev_piv = piv_idx
#         if word in s:
#             piv_idx += len(word)
        
#         if len(s) == piv_idx or piv_idx - prev_piv is len(word):
#             return True

# print(wordBreak2("catsandog",
# ["cats","dog","sand","and","cat"]))

# Start from the back and mark true false places for keys
def wordBreak3(s: str, wordDict: [str]) -> bool:

    dp = [False] * (len(s) + 1)
    dp[len(s)] = True # Base case to true out of bounds of string

    print(dp)

    # Starting at end
    print(len(s) - 1)
    # Starts at len - 1 which is 7 the starting numbers, then counds down to include 0 (thats why its negative -1 doeesnt include -1 in count and -1 tells it to count in reverse)
    for i in range(len(s) - 1, -1, -1):
        print("New Loop--------" , end="")
        print(i)
        for w in wordDict:
            # There are enough characters in s for us to compare to word ,  current index word + length of word
            print('Word Loop ------------- ')
            print("first condition")
            print(i + len(w), end="")
            print(' < ', end="")
            print(len(s))
            print("second condition")
            print(s[i: i + len(w)], end=" ")

            print(w)
            if (i + len(w) <= len(s)) and s[i: i + len(w)] == w:
                print("FOUND MATCH")
                print(i+ len(w))
                print(dp[i+ len(w)])
                dp[i] = dp[i+ len(w)]
                
                print(dp)
            # After it finds a match breaks to new set of checks 
            if dp[i]:
                print("BREAK")
                break
    
    print(dp)
    return dp[0]


# print(wordBreak3("leetcode",
# ["leet","code"]))

print(wordBreak3("catsandog",
["cats","dog","sand","and","cat"]))