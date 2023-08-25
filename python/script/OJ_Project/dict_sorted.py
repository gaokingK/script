from collections import OrderedDict


def find_good(dict_obj1, dict_obj2):
    dict_obj1.update(dict_obj2)
    all_score = dict_obj1
    res = OrderedDict()
    for _ in range(4):
        name, score = "", 0
        for key, value in all_score.items():
            if value > score:
                name, score = key, value
        all_score.pop(name)
        res.update({name: score})

    print(res)


if __name__ == '__main__':
    score_a = {"user1": 90, "user2": 70}
    score_b = {"user3": 89, "user4": 40, "user5": 22, "user6": 98}
    find_good(score_a, score_b)

    pass
