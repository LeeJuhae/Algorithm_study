def solution(room, molds):
    tile = [[e+1, n+1] for e in range(room[0]) for n in range(room[1])]
    for i,mold in enumerate(molds):
        if mold in tile:
            tile.pop(tile.index(mold))
        if i != 0:
            if [molds[i-1][0]+1,molds[i-1][1]+1] in tile:
                tile.pop(tile.index([molds[i-1][0]+1,molds[i-1][1]+1]))
            if [molds[i-1][0]+1,molds[i-1][1]-1] in tile:
                tile.pop(tile.index([molds[i-1][0]+1,molds[i-1][1]-1]))
            if [molds[i-1][0]-1,molds[i-1][1]+1] in tile:
                tile.pop(tile.index([molds[i-1][0]-1,molds[i-1][1]+1]))
            if [molds[i-1][0]-1,molds[i-1][1]-1] in tile:
                tile.pop(tile.index([molds[i-1][0]-1,molds[i-1][1]-1]))                             
    return "yes" if len(tile) == 0 else "no"

print(solution([3,3],[[1,1],[1,2],[2,1],[2,2],[3,1],[3,2]]))
print(solution([3,3],[[1,1],[2,2]]))