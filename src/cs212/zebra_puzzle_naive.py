# Solution of Einstein's Zebra Puzzle (http://en.wikipedia.org/wiki/Zebra_Puzzle)

import itertools


def imright(h1, h2):
    return h1 - h2  == 1


def nextto(h1, h2):
    return abs(h1 - h2) == 1


def zebra_puzzle_slow():
    houses = [first, _, middle, _, _] = [1, 2, 3, 4, 5]
    orderings = list(itertools.permutations(houses))
    return next((WATER, ZEBRA)
                for (Englishman, Spaniard, Ukranian, Japanese, Norwegian) in orderings
                for (red, green, ivory, yellow, blue) in orderings
                for (dog, snails, fox, horse, ZEBRA) in orderings
                for (coffee, tea, milk, oj, WATER) in orderings
                for (OldGold, Kools, Chesterfields, LuckyStrike, Parliaments) in orderings
                if Englishman is red
                if Spaniard is dog
                if coffee is green
                if Ukranian is tea
                if imright(green, ivory)
                if OldGold is snails
                if Kools is yellow
                if milk is middle
                if Norwegian is first
                if nextto(Chesterfields, fox)
                if nextto(Kools, horse)
                if LuckyStrike is oj
                if Japanese is Parliaments
                if nextto(Norwegian, blue)
                )


if __name__ == '__main__':
    print zebra_puzzle_slow()
