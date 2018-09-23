#!/usr/bin/env python3
import random


"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']
reflectmoves1 = ''
cyclemoves = ''


"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    scores = 0

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


def beats(one, two):
    winner = ((one == 'rock' and two == 'scissors')
              or (one == 'scissors' and two == 'paper')
              or (one == 'paper' and two == 'rock'))
    return (winner)


class RandomPlayer(Player):
    def move(self):
        randomnumber = random.randint(0, 2)
        return moves[randomnumber]


class HumanPlayer(Player):
    def move(self):
        error = 1
        while (error == 1):
            try:
                movenumber = int(input("Enter step number to move? "), 8)
                error = 0
                pass
            except Exception as e:
                print("You have entered invalid number, please try again")
                pass

        if(movenumber > 2 or movenumber < 0):
            print("The step number should from 0 to 2 ")
            movenumber = int(input("Enter step number to move? "), 8)
        return moves[movenumber]


class ReflectPlayer:
    scores = 0

    def move(self):
        if(reflectmoves1 == ''):
            return moves[random.randint(0, 2)]
        else:
            return reflectmoves1

    def learn(self, my_move, their_move):
        global reflectmoves1
        reflectmoves1 = their_move
        pass


class CyclePlayer:
    scores = 0

    def move(self):
        if(cyclemoves == ''):
            return moves[random.randint(0, 2)]
        elif ((moves.index(cyclemoves)+1) > 2):
            return moves[0]
        else:
            return moves[moves.index(cyclemoves)+1]

    def learn(self, my_move, their_move):
        global cyclemoves
        cyclemoves = my_move
        pass


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"You: {move1}  Computer: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        winner = beats(move1, move2)
        if (move1 == move2):
            print("winner: No Winner")
        elif(winner):
            print("winner: You")
            self.p1.scores = self.p1.scores + 1
        else:
            print("winner: Computer")
            self.p2.scores = self.p2.scores + 1

    def play_game(self):
        print("Game start!")
        while((self.p1.scores-self.p2.scores) < 3
                and (self.p2.scores-self.p1.scores) < 3):
            print(f"Round {round}:")
            self.play_round()

        if(self.p1.scores > self.p2.scores):
            print("You are ahead with 3 scores")
        else:
            print("Computer is ahead with 3 scores")

        print("Game over!")


if __name__ == '__main__':
    game = Game(HumanPlayer(), RandomPlayer())
    game.play_game()
