def is_palindrome(s):
    # Remove spaces and convert to lowercase for uniformity
    s = s.replace(" ", "").lower()

    # Check if the string is equal to its reverse
    return s == s[::-1]


# Test the function
test_str = "A man a plan a canal Panama"
if is_palindrome(test_str):
    print(f'"{test_str}" is a palindrome.')
else:
    print(f'"{test_str}" is not a palindrome.')
