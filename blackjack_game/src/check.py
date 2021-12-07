
class Checks():
    def __init__(self, player, dealer):
        self.player_hand = player
        self.dealer_hand = dealer

    def count_player(self):
        count = 0
        for i in self.player_hand:
            count = count+int(i[0])
        return count

    def count_dealer(self):
        count = 0
        for i in self.dealer_hand:
            count = count+int(i[0])
        return count
