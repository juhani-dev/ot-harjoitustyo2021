
class Checks():
    """Luokka laskee pelaajan ja jakajan sen hetkisten korttien summan.

    """
    def __init__(self, player, dealer):
        """luokan konstruktori

        Args:
            player ([type]): pelaajan sen hetkiset kortit lista muodossa
            dealer ([type]): jakajan sen hetkiset kortit lista muodossa
        """
        self.player_hand = player
        self.dealer_hand = dealer

    def count_player(self):
        """Laskee listasta  pelaajan korttien summan

        Returns:
            [type]: korttien arvojen summan
        """
        count = 0
        ace = False
        for i in self.player_hand:
            count = count+int(i[0])
            if int(i[0]) == 14:
                ace =True
        if ace is True and count > 21:
            count =count -13
        return count

    def count_dealer(self):
        """Laskee listasta jakajan korttien summan

        Returns:
            [type]: korttien arvojen summan
        """
        count = 0
        ace = False
        for i in self.dealer_hand:
            count = count+int(i[0])
            if int(i[0]) == 14:
                ace =True
        if ace is True and count > 21:
            count =count -13
        return count
