#!/usr/bin/env python3
import random

shuffledDeck = {11: 12, 10: 48, 9: 12, 8: 12, 7: 12, 6: 12, 5: 12, 4: 12, 3: 12, 2: 12}
deck = {11: 12, 10: 48, 9: 12, 8: 12, 7: 12, 6: 12, 5: 12, 4: 12, 3: 12, 2: 12}
cards = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
totalCard = 156
runCount = 0

def playerStrat(hand, upcard):
    if hand >= 17:
        return 2
    elif 13 <= hand <= 16:
        if 2 <= upcard <= 6:
            return 2
        else:
            return 1
    elif hand == 12:
        if 4 <= upcard <= 6:
            return 2
        else:
            return 1
    elif hand == 11:
        return 3
    elif hand == 10:
        if 2 <= upcard <= 9:
            return 3
        else:
            return 1
    elif hand == 9:
        if 3 <= upcard <= 6:
            return 3
        else:
            return 1
    elif hand <= 8:
        return 1

def blackjack(card):
    dealer, player = [], []
    dSum, pSum = 0, 0
    global totalCard, runCount
    double = False

    for i in range(2):
        dCard, pCard = 0, 0
        while dCard not in deck or deck[dCard] == 0:
            dCard = random.choice(cards)
        while pCard not in deck or deck[pCard] == 0:
            pCard = random.choice(cards)

        if 2 <= dCard <= 6: runCount += 1
        elif dCard == 10 or dCard == 11: runCount -= 1

        if 2 <= pCard <= 6: runCount += 1
        elif pCard == 10 or pCard == 11: runCount -= 1

        dealer.append(dCard)
        dSum += dCard
        deck[dCard] -= 1
        totalCard -= 1

        player.append(pCard)
        pSum += pCard
        deck[pCard] -= 1
        totalCard -= 1

    upcard = dealer[0]
    strat = playerStrat(pSum, upcard)

    while True:
        if strat == 1:
            while pCard not in deck or deck[pCard] == 0:
                pCard = random.choice(cards)
            player.append(pCard)
            pSum += pCard
            deck[pCard] -= 1
            totalCard -= 1
            strat = playerStrat(pSum, upcard)
        elif strat == 2:
            while dSum <= 16:
                while dCard not in deck or deck[dCard] == 0:
                    dCard = random.choice(cards)
                dealer.append(dCard)
                dSum += dCard
                deck[dCard] -= 1
                totalCard -= 1

            if not double:
                if pSum == 21: return 1
                elif pSum > 21: return 2
                elif dSum > 21: return 1
                elif pSum > dSum: return 1
                elif dSum > pSum: return 2
                else: return 3
            else:
                if pSum == 21: return 4
                if pSum > 21: return 5
                elif dSum > 21: return 4
                elif pSum > dSum: return 4
                elif dSum > pSum: return 5
                else: return 3
        else:
            while pCard not in deck or deck[pCard] == 0:
                pCard = random.choice(cards)
            player.append(pCard)
            pSum += pCard
            deck[pCard] -= 1
            totalCard -= 1
            strat = playerStrat(pSum, upcard)
            double = True

def shuffle():
    global deck, totalCard, runCount
    deck = shuffledDeck.copy()
    totalCard = 156
    runCount = 0

if __name__ == "__main__":
    wins, losses, dWin, dLoss, push = 0, 0, 0, 0, 0
    money = 10000

    print("Start: %s" % money)

    for i in range(500):
        if totalCard <= 20:
            shuffle()

        totDecks = -(-totalCard // 52)
        trueCount = runCount // totDecks
        betUnit = money // 1000
        opBet = 0
        if trueCount - 1 > 0:
            opBet = (trueCount - 1) * betUnit
        else:
            opBet = betUnit

        res = blackjack(deck)
        if res == 1:
            wins += 1
            money += opBet
        elif res == 2:
            losses += 1
            money -= opBet
        elif res == 4:
            wins += 1
            dWin += 1
            money += 2 * opBet
        elif res == 5:
            losses += 1
            dLoss += 1
            money -= 2 * opBet
        else:
            push += 1

    print("Wins: %s" % wins)
    print("Losses: %s" % losses)
    print("Doubled Wins: %s" % dWin)
    print("Doubled Losses: %s" % dLoss)
    print("Push: %s" % push)
    print("Money: %s" % money)


