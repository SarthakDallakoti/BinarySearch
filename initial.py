# Example dictionary (in a real-world scenario, this list would be much larger and contain all valid words)
dictionary = sorted(["apple", "banana", "cherry", "date", "fig", "grape", "kiwi"])

def binary_search_word(word, word_list):
    """Return True if word exists in word_list using binary search, False otherwise."""
    left, right = 0, len(word_list) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if word_list[mid] == word:
            return True
        elif word_list[mid] < word:
            left = mid + 1
        else:
            right = mid - 1
            
    return False

# Testing the spell checker
word_to_check = "kiwii"
if not binary_search_word(word_to_check, dictionary):
    print(f"'{word_to_check}' might be a misspelled word!")
else:
    print(f"'{word_to_check}' is a valid word!")
