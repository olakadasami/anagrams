# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagrams(word, anagram):
    # [assignment] Add your code here
    if (sorted(word) == sorted(anagram)):
        print('true')
        return True
    else:
        print('false')
        return False

find_anagrams("below", "check")
