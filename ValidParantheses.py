def validParantheses(s: str) -> bool:
    stack_piece = []
    string_length = len(s)
    for i in range(string_length):
        if s[i] == "(":
            stack_piece.append(s[i])
        if s[i] == ")":
            if not stack_piece:
                return False
            if stack_piece[-1] != "(":
                return False
            else:
                stack_piece.pop(-1)

        elif s[i] == "[":
            stack_piece.append(s[i])
        if s[i] == "]":
            if not stack_piece:
                return False
            if stack_piece[-1] != "[":
                return False
            else:
                stack_piece.pop(-1)

        elif s[i] == "{":
            stack_piece.append(s[i])
        if s[i] == "}":
            if not stack_piece:
                return False
            if stack_piece[-1] != "{":
                return False
            else:
                stack_piece.pop(-1)

    if not stack_piece:
        return True

    return False


if __name__ == "__main__":
    test = "({[]})[()]{()[]}"
    test_false = "([)]"
    print(validParantheses(test))
    print(validParantheses(test_false))
