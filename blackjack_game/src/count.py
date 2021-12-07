def count_player(hand):
    count = 0
    for i in hand:
        count = count+int(i[0])
    return count


def count_dealer(hand):
    count = 0
    for i in hand:
        count = count+int(i[0])
    return count
