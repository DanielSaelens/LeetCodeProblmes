def lengthOfLongestSubstring(s: str) -> int:
    counter = 0
    stack_letter = []
    string_length = len(s)

    for i in range(string_length):
        if s[i] not in stack_letter:
            stack_letter.append(s[i])
        elif s[i] in stack_letter:
            position = stack_letter.index(s[i])
            stack_letter = stack_letter[position + 1:]
            stack_letter.append(s[i])
        counter = max(counter, len(stack_letter))

    return counter


if __name__ == "__main__":
    print(lengthOfLongestSubstring("pwwkew"))
    print(lengthOfLongestSubstring("S"))


# Need to find a way so the substring, and no repeats are kept.
# 1. We need a way to handle we found two of the same letters.
# 2. If we do, we have to figure out which one to discard and which to keep.
# 3. We found two letters, we need to decide if the left side is longer, or the right side
# 4. How we do that? TBA
# 5. Maybe can do two variable's that has left side and the right side, and compare the two.
# 6. Maybe a set for finding out the repeating characters.
# 7. s[:i], s[i + 1:] how to check left and right
# 8. Need a way to check for duplicates still.
