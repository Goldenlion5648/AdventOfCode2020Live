from collections import *
from math import *

with open("input22.txt") as f:
    # a = list(map(int,f.read().strip().split("\n")))
    a = f.read().strip().split("\n")


print(a)
player1 = a[1:a.index("")]
player2 = a[a.index("")+2:]

# print(player2)
player1 = deque(map(int,player1))
player2 = deque(map(int,player2))
# while len(player1)> 0 and len(player2) > 0:
#     c = player1.popleft()
#     d = player2.popleft()
#     if c > d:
#         player1.append(c)
#         player1.append(d)
#     else:
#         player2.append(d)
#         player2.append(c)

# score = 0
# if len(player1):
#     pos = 1
#     print("a", player1)
#     while pos < len(player1):
#         score += player1[-pos] * pos
#         pos += 1
# else:
#     print(player2)
#     pos = 1
#     while pos <= len(player2):
#         score += player2[-pos] * pos
#         pos += 1
# print(score)
def recursiveCombat(player1, player2, c, d, seen):
    newP1 = player1.copy()
    newP2 = player2.copy()
    temp = (newP1, newP2)
    if temp not in seen:
        seen.append(temp)
    else:
        return True, False, newP1, newP2
    if len(newP1) >= c and len(newP2) >= d:
        newDeck1 = deque([newP1.popleft() for i in range(c)])
        newDeck2 = deque([newP2.popleft() for i in range(d)])
        print("newDeck1", newDeck1)
        print("newDeck2", newDeck2)
        w1, w2, newP1, newP2 = playNormal(newDeck1, newDeck2, seen)
        return w1, w2, newP1, newP2
    else:
        assert False

def playNormal(player1a, player2b, seen):
    new1 = player1a.copy()
    new2 = player2b.copy()
    print("normal", new1)
    print("normal2", new2)
    if len(new1) == 0:
        return False, True, new1, new2
    if len(new2) == 0:
        return True, False, new1, new2
    c = new1.popleft()
    d = new2.popleft()
    p1 = True
    p2 = True
    print("1 played", c)
    print("2 played", d)
    if len(new1) >= c and len(new2) >= d:
        print("playing recur")
        s1 = []
        if len(seen):
            s1 = seen.copy()
        p1, p2, new1, new2 = recursiveCombat(new1, new2, c, d, s1)
    else:
        print("played normal")
        if c > d:
            new1.append(c)
            new1.append(d)
            print("one won round")
        else:
            new2.append(d)
            new2.append(c)
            print("two won round")
    if p1 == False:
        return False, True, new1, new2
    elif p2 == False:
        return True, False, new1, new2
    # temp = (new1.copy(), new2.copy())
    # if temp in seen:
    #     print("player 1 wins")
    #     print("temp", temp)
    #     print(seen)
    #     oneWins = True
    #     return True, False, new1, new2
    # else:
    #     seen.append(temp)
    return True, True, new1, new2

oneWins = False
count = 0
while len(player1)> 0 and len(player2) > 0:
    count += 1
    done1, done2, player1, player2 = playNormal(player1, player2, [])
    if done1 == False:
        break
    elif done2 == False:
        oneWins = True
        break
    print(count)

print(player1)
print(player2)


# score = 0
# if len(player1):
#     pos = 1
#     print("a", player1)
#     while pos < len(player1):
#         score += player1[-pos] * pos
#         pos += 1
# else:
#     print(player2)
#     pos = 1
#     while pos <= len(player2):
#         score += player2[-pos] * pos
#         pos += 1
'''
Before either player deals a card, if there was a previous round in this game that had exactly the same cards in the same order in the same players' decks, the game instantly ends in a win for player 1. Previous rounds from other games are not considered. (This prevents infinite games of Recursive Combat, which everyone agrees is a bad idea.)
Otherwise, this round's cards must be in a new configuration; the players begin the round by each drawing the top card of their deck as normal.
If both players have at least as many cards remaining in their deck as the value of the card they just drew, the winner of the round is determined by playing a new game of Recursive Combat (see below).
Otherwise, at least one player must not have enough cards left in their deck to recurse; the winner of the round is the player with the higher-value card.'''