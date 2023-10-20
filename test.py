from initial3 import get_suggestions

def run_tests():
    test_cases = {
        'teh': ['the', 'tech'],
        'beutiful': ['beautiful', 'bountiful'],
        'recieve': ['receive', 'relieve'],
        'seperated': ['separated', 'separate'],
        'occured': ['occurred', 'occurs'],
        'amoung': ['among', 'amount'],
        'appologies': ['apologies', 'apology'],
        'arguement': ['argument'],
        'commited': ['committed', 'commits'],
        'definately': ['definitely'],
        'dissapear': ['disappear', 'disappears'],
        'existance': ['existence'],
        'familar': ['familiar'],
        'futher': ['further', 'future'],
        'happend': ['happened', 'happens'],
        'knowlege': ['knowledge'],
        'ocassion': ['occasion', 'occasions'],
        'publically': ['publicly'],
        'realy': ['really', 'real'],
        'appla': ['apple', 'apply']
    }

    passed_tests = 0
    total_tests = len(test_cases)

    for input_word, expected_suggestions in test_cases.items():
        actual_suggestions = get_suggestions(input_word)
        if actual_suggestions == expected_suggestions:
            print(f"Test for '{input_word}' PASSED!")
            passed_tests += 1
        else:
            print(f"Test for '{input_word}' FAILED! Got {actual_suggestions}, expected {expected_suggestions}.")

    print(f"\nResults: {passed_tests}/{total_tests} tests passed.")

if __name__ == '__main__':
    run_tests()

