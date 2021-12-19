
def solution(test_str):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    reverse_alpha = "zyxwvutsrqponmlkjihgfedcba"
    result = ""
    for char in test_str:
        if char.islower():
            index = alpha.index(char)
            # char = alphabet[len(alphabet) - index]
            result += reverse_alpha[index]
        else:
            result += char
    return result


print(solution("wrw blf hvv ozhg mrtsg'h vkrhlwv?"))
