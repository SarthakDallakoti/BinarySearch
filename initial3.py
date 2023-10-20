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


def get_suggestions(user_input):
    # Define the Levenshtein distance function
    def levenshtein_distance(s1, s2):
        if len(s1) > len(s2):
            s1, s2 = s2, s1

        distances = range(len(s1) + 1)
        for i2, c2 in enumerate(s2):
            distances_ = [i2+1]
            for i1, c1 in enumerate(s1):
                if c1 == c2:
                    distances_.append(distances[i1])
                else:
                    distances_.append(1 + min((distances[i1], distances[i1 + 1], distances_[-1])))
            distances = distances_
        return distances[-1]

    # Fetch the word from the database
    cursor.execute("SELECT word FROM dictionary WHERE word=?", (user_input,))
    result = cursor.fetchone()

    if result:
        return user_input  # The word is spelled correctly

    # Fetch words from the database that start with the first letter of the user input
    prefix = user_input[0]
    cursor.execute("SELECT word FROM dictionary WHERE word LIKE ?", (prefix + '%',))
    close_words = [row[0] for row in cursor.fetchall()]

    # Find suggestions based on Levenshtein distance
    suggestions = sorted(
        [word for word in close_words if levenshtein_distance(word, user_input) <= 3],
        key=lambda x: (levenshtein_distance(x, user_input), -len(x))
    )

    # Return the top suggestion, or None if no suggestions are available
    return suggestions[:2]

# User interactive section
if __name__ == '__main__':
    while True:
        user_input = input("Enter a word (or 'exit' to quit): ").strip()
        
        if user_input.lower() == 'exit':
            break

        suggestion = get_suggestions(user_input)
        if suggestion:
            if suggestion == user_input:
                print(f"'{user_input}' is spelled correctly!")
            else:
                print(f"'{user_input}' might be misspelled! Did you mean: '{suggestion}'?")
        else:
            print(f"No suggestions available for '{user_input}'.")
