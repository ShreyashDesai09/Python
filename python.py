def is_palindrome(ref):
    ref = ref.lower().replace(" ", "")  # optional: make lowercase and remove spaces
    i = 0
    j = len(ref) - 1

    while i < j:
        if ref[i] != ref[j]:
            return False
        i += 1
        j -= 1
    return True

# Example usage
A = "racecar"
print(is_palindrome(A))  # Output: True
