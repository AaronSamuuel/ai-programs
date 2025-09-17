from itertools import permutations

def solve_cryptarithmetic(puzzle):
    """
    Solves the cryptarithmetic puzzle.
    puzzle: a string containing the puzzle in the form of "WORD + WORD = RESULT"
    Returns a dictionary mapping letters to digits, or None if no solution is found.
    """
    # Split into words
    left, result = puzzle.split("=")
    words = left.split("+")
    words = [w.strip() for w in words]
    result = result.strip()

    # Collect all unique letters
    letters = set("".join(words) + result)
    if len(letters) > 10:
        return None  # Can't map to digits (0–9)

    letters = list(letters)

    # Try all permutations of digits for letters
    for perm in permutations(range(10), len(letters)):
        mapping = dict(zip(letters, perm))

        # Skip if any word starts with zero
        if any(mapping[word[0]] == 0 for word in words + [result]):
            continue

        # Convert words to numbers
        word_values = [int("".join(str(mapping[c]) for c in word)) for word in words]
        result_value = int("".join(str(mapping[c]) for c in result))

        # Check equation
        if sum(word_values) == result_value:
            return mapping

    return None


# Example usage
puzzle = "SEND + MORE = MONEY"
mapping = solve_cryptarithmetic(puzzle)

if mapping:
    print("Solution mapping:", mapping)

    # Show solved equation
    left, result = puzzle.split("=")
    words = left.split("+")
    words = [w.strip() for w in words]
    result = result.strip()

    solved_words = ["".join(str(mapping[c]) for c in w) for w in words]
    solved_result = "".join(str(mapping[c]) for c in result)

    print(f"{' + '.join(solved_words)} = {solved_result}")
else:
    print("No solution found.")
