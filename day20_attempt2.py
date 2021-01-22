from collections import *
from math import *
import random
import copy
import re
with open("input20.txt") as f:
    a = f.read().strip().split("\n\n")

class Tile:
    def __init__(self, data):
        if data != None:
            self.id = int(data[0].split()[1][0:-1])
            self.rows = [list(i) for i in data[1:]]
            self.get_possible_sides()
            self.matches = set()
    def get_possible_sides(self):
        self.sides = []
        self.sides.append(self.rows[0])
        self.sides.append([i[-1] for i in self.rows])
        self.sides.append(self.rows[-1])
        self.sides.append([i[0] for i in self.rows])
        self.sides.append(list(reversed(self.rows[0])))
        self.sides.append(list(reversed([i[-1] for i in self.rows])))
        self.sides.append(list(reversed(self.rows[-1])))
        self.sides.append(list(reversed([i[0] for i in self.rows])))
    def rotate90(self):
        temp = []
        for i in range(len(self.rows)):
            cur = [self.rows[j][i] for j in range(len(self.rows)-1, -1, -1)]
            temp.append(cur)
        self.rows = copy.deepcopy(temp)
        self.get_possible_sides()
    def print_rows(self):
        for i in self.rows:
            print("".join(i))
        print()
    def flip(self):
        temp = copy.deepcopy(self.rows)
        for i in range(len(self.rows)//2):
            temp[i], temp[-i-1] = temp[-i-1], temp[i] 
        self.rows = copy.deepcopy(temp)
        self.get_possible_sides()
    def remove_borders(self):
        # temp = copy.deepcopy(rows)
        for i in range(1, len(self.rows)):
            self.rows[i] = self.rows[i][1:-1]
        self.rows.pop()
        self.rows.pop(0)
        
a = [i.split("\n") for i in a]
tiles = [Tile(i) for i in a]

print("len of tiles", len(tiles))
# for i in tiles:
#     for j in i.sides:
#         print("".join(j))
#     print()
piece_lookup = {i.id: i for i in tiles}
# tiles = copy.deepcopy(tiles)
answer_pieces = []
found_count = 0
for i in range(len(tiles)):
    # found = False
    sides_found = 0
    for j in range(len(tiles)):
        if i == j:
            continue
        found =  False
        for k in range(8):
            for w in range(8):
                if tiles[i].sides[k] == tiles[j].sides[w]:
                    found = True
                    sides_found += 1
                    tiles[i].matches.add(tiles[j])
                    tiles[j].matches.add(tiles[i])

                    # break
            # if found:
            #     break

    # print("sides matching", sides_found)
    if sides_found == 4:
        answer_pieces.append(tiles[i].id)

# for i in answer_pieces:
#     print(i)
print("part 1", prod(answer_pieces))

[print("".join(i)) for i in tiles[0].rows]
tiles[0].flip()
print()
[print("".join(i)) for i in tiles[0].rows]

print("answer_pieces", answer_pieces)
start = [i for i in tiles if i.id == answer_pieces[0]][0]
print("start", start)
print([i.id for i in start.matches])
print(start.id)

def make_piece_fit(piece, placed_pieces, height, side1=1, side2=3):
    print("checking piece id", piece.id)
    print("trying to match against", placed_pieces[height][-1].sides[side1])
    if placed_pieces[height][-1].sides[side1] == piece.sides[side2]:
        return True
    piece.print_rows()
    # keep_turning = all([piece.sides[0] in j.sides for j in piece.matches]) or any([piece.sides[-1] in j.sides for j in piece.matches])
    # if not keep_turning:
    #     return 
    for i in range(3):
        piece.rotate90()
        piece.print_rows()
        if placed_pieces[height][-1].sides[side1] == piece.sides[side2]:
            return True
    #bring back to start
    piece.rotate90()
    piece.flip()
    if placed_pieces[height][-1].sides[side1] == piece.sides[side2]:
        return True
    for i in range(3):
        piece.rotate90()
        if placed_pieces[height][-1].sides[side1] == piece.sides[side2]:
            return True
    # print("did not fit")
    return False

cur_y = 0
# cur_x = 0
filled_board = [[start]]
print("start")
start.print_rows()
print("end")
print(start.matches)

def show_progress(filled_board):
    print("found so far:")
    for i in filled_board:
        print("new row")
        for j in i:
            print(j.id)
            j.print_rows()
            # print()

used_tiles = {start}
num_placed = 1
while True:
    tiles_to_check = filled_board[-1][0].matches - used_tiles
    print("tiles to check", tiles_to_check)
    for i in tiles_to_check:
        does_fit = make_piece_fit(i, filled_board, -1, 2, 0)
        if does_fit:
            print("added", i.id)
            used_tiles.add(i)
            filled_board.append([i])
            num_placed += 1
            break
    if filled_board[-1][0].id in answer_pieces:
        break

print("filled_board", filled_board)
show_progress(filled_board)

print("len of filled_board", len(filled_board))
# assert False
while num_placed < len(tiles):
    print("cur_y", cur_y)
    tiles_to_check = filled_board[cur_y][-1].matches - used_tiles
    # print("tiles to check", tiles_to_check)
    if 1< len(filled_board[cur_y]) and cur_y < len(filled_board) -1 and len(tiles_to_check) == 1:
        cur_y += 1
        continue
    for i in tiles_to_check:
        # temp = copy.deepcopy(i)
        does_fit = make_piece_fit(i, filled_board, cur_y, 1, 3)
        if does_fit:
            # print("it fit!")
            print("added", i.id)
            filled_board[cur_y].append(i)
            num_placed += 1
            used_tiles.add(i)
            break

    print("num_placed", num_placed)
    print("cur_y", cur_y)


# show_progress(filled_board)
for i in filled_board:
    for j in i:
        j.remove_borders()
print("borders removed:")
show_progress(filled_board)

picture = []
# for i in filled_board:
    # for j in i:

tile_dim = len(filled_board[0][0].rows)
for i in range(len(filled_board)):
    for x in range(tile_dim):
        picture.append("".join(["".join(j.rows[x]) for j in (filled_board[i])]))

print(picture)
picture_tile = Tile(None)
picture_tile.rows = [list(i) for i in picture]
picture_tile.get_possible_sides()

def search_for_monster(board):
    monster_count = 0
    for i in range(1, len(board)-3):
        for j in range(len(board[0])-20):
            if board[i][j] == "#":
                slice1="".join(board[i-1][j:j+20])
                slice2="".join(board[i][j:j+20])
                slice3="".join(board[i+1][j:j+20])
                print(slice1)
                print(slice2)
                print(slice3)
                if \
                re.fullmatch("..................#.", slice1) and \
                re.fullmatch("#....##....##....###", slice2) and \
                re.fullmatch(".#..#..#..#..#..#...", slice3):
                    monster_count += 1
    return monster_count
                                                #                             
                              #    ##    ##    ###
                               #  #  #  #  #  #   

test_input=""".####...#####..#...###..
#####..#..#.#.####..#.#.
.#.#...#.###...#.##.##..
#.#.##.###.#.##.##.#####
..##.###.####..#.####.##
...#.#..##.##...#..#..##
#.##.#..#.#..#..##.#.#..
.###.##.....#...###.#...
#.####.#.#....##.#..#.#.
##...#..#....#..#...####
..#.##...###..#.#####..#
....#.##.#.#####....#...
..##.##.###.....#.##..#.
#...#...###..####....##.
.#.##...#.##.#.#.###...#
#.###.#..####...##..#...
#.###...#.##...#.######.
.###.###.#######..#####.
..##.#..#..#.#######.###
#.#..##.########..#..##.
#.#####..#.#...##..#....
#....##..#.#########..##
#...#.....#..##...###.##
#..###....##.#...##.##.#"""
test_input = [list(i) for i in test_input.split("\n")]
print(test_input)
# print(search_for_monster(picture_tile.rows))
found_orientation = False
count = 0
for i in range(4):
    count = search_for_monster(picture_tile.rows)
    if count != 0:
        found = True
        break
    picture_tile.rotate90()
if found == False:
    picture_tile.flip()
    for i in range(4):
        count = search_for_monster(picture_tile.rows)
        if count != 0:
            found = True
            break
        picture_tile.rotate90()

print("monster_count", count)
#count hashtags
hash_count = sum([row.count("#") for row in picture_tile.rows])

print("hash_count", hash_count)
print("part 2:", hash_count - count*15)
    # picture.append("".join(filled_board[i//tile_dim]))
# print("found so far:")
# for i in filled_board[cur_y]:
#     i.print_rows()
#     print()
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   
# print([i.id for i in piece_lookup[1327].matches])


# while 