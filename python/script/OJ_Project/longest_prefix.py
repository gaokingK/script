def calc_longest_str(str_list):
    res = ""
    for str_tup in zip(*str_list):
        if len(set(str_tup)) == 1:
            res += str_tup[0]
        else:
            break
    return res


if __name__ == '__main__':
    test_data = ["food", "fook", "fo"]
    print(calc_longest_str(test_data))
