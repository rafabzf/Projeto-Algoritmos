def is_anagram(first_string, second_string):
    word1 = list(first_string.lower())
    word2 = list(second_string.lower())
    sort_word(word1)
    sort_word(word2)
    if word1 != word2 or len(first_string) == 0 or len(second_string) == 0:
        return ("".join(word1), "".join(word2), False)
    else:
        return ("".join(word1), "".join(word2), True)


def sort_word(word, start=0, end=None):
    if end is None:
        end = len(word)
    if (end - start) > 1:
        middle = (start + end) // 2
        sort_word(word, start, middle)
        sort_word(word, middle, end)
        merge(word, start, middle, end)


def merge(word, start, middle, end):
    left = word[start:middle]
    r = word[middle:end]
    l_i, r_i = 0, 0

    for index in range(start, end):
        if l_i >= len(left):
            word[index] = r[r_i]
            r_i = r_i + 1
        elif r_i >= len(r):
            word[index] = left[l_i]
            l_i = l_i + 1
        elif left[l_i] < r[r_i]:
            word[index] = left[l_i]
            l_i = l_i + 1
        else:
            word[index] = r[r_i]
            r_i = r_i + 1


print(is_anagram("", ""))
