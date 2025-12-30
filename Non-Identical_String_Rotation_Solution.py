

#print("helllo world")


#hackerRank final version
#def isNonTrivialRotation(s1, s2):
    #if len(s1) != len(s2):
        #return False
    #if s1 == s2:
        #return False
    #return s2 in (s1 + s1)


#print("I hate everything")

#final version with testing capabilities

def isNonTrivialRotation(s1, s2):
    # Different lengths cannot be rotations
    if len(s1) != len(s2):
        return False

    # Identical strings are trivial rotations
    if s1 == s2:
        return False

    # Rotation check
    return s2 in (s1 + s1)


def test_is_non_trivial_rotation():
    test_cases = [
        ("abcde", "cdeab", 1),
        ("hello", "lohel", 1),
        ("abcde", "abcde", 0),
        ("a", "a", 0),
        ("a", "b", 0),
        ("abc", "ab", 0),
        ("abc", "abcd", 0),
    ]

    all_passed = True

    for s1, s2, expected in test_cases:
        result = int(isNonTrivialRotation(s1, s2))
        print(f"Testing ('{s1}', '{s2}') → Expected: {expected}, Got: {result}")

        if result != expected:
            all_passed = False

    if all_passed:
        print("\n✅ All tests passed successfully!")
    else:
        print("\n❌ All tests did not pass")


if __name__ == "__main__":
    test_is_non_trivial_rotation()

