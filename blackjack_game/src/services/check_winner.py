

class Winner():
    """Luokka millä tarkistetaan onko jaon voittaja pelaaja vai jakaja
    """
    def __init__(self,player,dealer):
        """Luokan konstruktori mihin tuodaan pelaajan ja jakajan korttien summat

        Args:
            player : pelaajan korttien yhteen laskettu summa
            dealer :  jakajan korttien yhteen laskettu summa
        """
        self.player = player
        self.dealer = dealer
        self.winner = ""
    def get_winner(self):
        """ Tarkistaa kumpi käsi voittaa

        Returns:
             voittajan string muodossa
        """
        dealer_wins = "dealer wins"
        player_wins = "player wins"
        draw = "draw"

        if self.player == self.dealer:
            self.winner = dealer_wins
            if self.player == 21:
                self.winner = draw
        if self.player < 22 and self.dealer > 21:
            self.winner = player_wins
        if self.dealer < 22 and self.player > 21:
            self.winner = dealer_wins
        if self.dealer == 21 and self.player < 21:
            self.winner = dealer_wins
        if self.player == 21 and self.dealer < 21:
            self.winner = player_wins
        if self.player < 21 and self.dealer < 21:
            if self.player > self.dealer:
                self.winner = player_wins
            if self.player < self.dealer:
                self.winner = dealer_wins
        return self.winner
        