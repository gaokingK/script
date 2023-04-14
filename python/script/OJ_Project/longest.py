def calc_longest_prefix(str_list):
    res=""
    for con_letter_tup in zip(*str_list):
        if len(set(con_letter_tup)) == 1:
            res += con_letter_tup[0]
        else:
            break
    return res


if __name__ == '__main__':
    str_list = ["heddy", "hedy3","he"]
    print(calc_longest_prefix(str_list))
