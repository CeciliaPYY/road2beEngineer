
def reverseString(string):
    reverse_string = []
    n = len(string)
    for i in range(n-1, -1, -1):
        reverse_string.append(string[i])
    final_reverse_string = ''.join(reverse_string)

    return final_reverse_string

a = raw_input()
print(reverseString(a))
