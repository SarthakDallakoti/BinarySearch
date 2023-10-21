import sqlite3

# Connect to the existing SQLite database
conn = sqlite3.connect('dictionary.db')
cursor = conn.cursor()

# Ensure we have the table and it contains words. This is just to handle errors gracefully.
try:
    cursor.execute("SELECT COUNT(*) FROM dictionary")
    word_count = cursor.fetchone()[0]
    if word_count == 0:
        raise ValueError("The dictionary table is empty.")
except sqlite3.OperationalError:
    raise ValueError("The 'dictionary' table doesn't exist in the database.")


def check_word_spelling(word):
    word_lowercase = word.lower()
    cursor.execute("SELECT word FROM dictionary WHERE LOWER(word) = ?", (word_lowercase,))
    result = cursor.fetchone()
    if result:
        return True
    else:
        return False


def get_suggestions_for_word(word):
    word_lowercase = word.lower()
    
    def levenshtein_distance(s1, s2):
        if len(s1) > len(s2):
            s1, s2 = s2, s1

        distances = range(len(s1) + 1)
        for i2, c2 in enumerate(s2):
            distances_ = [i2 + 1]
            for i1, c1 in enumerate(s1):
                if c1 == c2:
                    distances_.append(distances[i1])
                else:
                    distances_.append(1 + min((distances[i1], distances[i1 + 1], distances_[-1])))
            distances = distances_
        return distances[-1]

    prefix = word_lowercase[0]
    cursor.execute("SELECT word FROM dictionary WHERE word LIKE ?", (prefix + '%',))
    close_words = [row[0] for row in cursor.fetchall()]

    suggestions = sorted(
        [w for w in close_words if levenshtein_distance(w.lower(), word_lowercase) <= 3 and w.lower() != word_lowercase],
        key=lambda x: (levenshtein_distance(x.lower(), word_lowercase), -len(x))
    )

    return suggestions[:2]

def check_sentence_spelling(user_sentence):
    words = user_sentence.split()
    misspelled_words = []
    feedback = []
    any_mistakes = False

    for word in words:
        if not check_word_spelling(word):
            any_mistakes = True
            misspelled_words.append(word)
            suggestion = get_suggestions_for_word(word)
            if suggestion:
                feedback.append(f"'{word}' might be misspelled! Did you mean: {', '.join(suggestion)}?")
            else:
                feedback.append(f"No suggestions available for '{word}'.")
    if not any_mistakes:
        feedback.append("The sentence is spelled correctly!")

    return not any_mistakes, misspelled_words, feedback

# User interactive section
if __name__ == '__main__':
    while True:
        user_sentence = input("Enter a sentence (or 'exit' to quit): ").strip()  # Do NOT convert the entire input to lowercase

        if user_sentence.lower() == 'exit':
            break

        words = user_sentence.split()
        any_mistakes = False
        for word in words:
            if not check_word_spelling(word):
                any_mistakes = True
                suggestion = get_suggestions_for_word(word)
                if suggestion:
                    print(f"'{word}' might be misspelled! Did you mean: {', '.join(suggestion)}?")
                else:
                    print(f"No suggestions available for '{word}'.")
        if not any_mistakes:
            print("The sentence is spelled correctly!")
