a,b,c = map(int,input().split())

person = [[int(x) for x in input().split()] for y in range(b)]

av = []

av_k = []

enter = 0

packing = 0

trash = 0

loc = []

sec = [0] * b

for k,i in enumerate(person):

    if i[0] == 1:

        if i[1] != 3:

            av += [[0,i[1]]]

            #av.append([0,i[1])

            av_k+=[[[0,i[1]],k]]

        else:

            av += [[0,3]]

            av += [[1,4]]

            #av.append[0,3])

            av_k.append([[0,3],k])

            av_k.append([[1,4],k])

    elif i == [2,3]:

        av += [[2,4]]

        av_k.append([[2,4],k])

    elif i[0] == 3:

        if i[1] != 3:

            av += [[4,i[1]]]

            #av.append([[4,i[1],k]])

            av_k += [[[4,i[1]],k]]

        else:

            av += [[3,4]]

            av += [[4,3]]

            av_k += [[[3,4],k]]

            av_k += [[[4,3],k]]

            #av.append([[3,4,k],[4,3,k]])



key = -1
while(True):
    if enter < c:
        for i in range(len(loc)):
            if loc[i] == [0,4]:
                loc[i] = [1,4]
            elif loc[i] == [4,4]:
                loc[i] = [4,3]
            elif loc[i][0] == 0:
                loc[i][1] = loc[i][1] + 1
            elif loc[i][1] == 4:
                loc[i][0] =  loc[i][0]  + 1
            elif loc[i][0] == 4:
                loc[i][1] =  loc[i][1]  -1
        enter += 1
        loc.append([0,0])
    for i in loc:
        if i in av:
            for v in av_k:
                if i in v:
                    key = v[1]
                    break
            if sec[key] == 0:
                loc.pop(loc.index(i))
                packing += 1
    if [4,0] in loc:
        loc.pop(loc.index(i))
        trash += 1
    if len(loc) == 0:
        print(packing)
        break
    for i in range(b):
        if i> 0:
            i -= 1
    print(loc)
