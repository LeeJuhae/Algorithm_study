import sys
sys.setrecursionlimit(10**6)

def findEmptyRoom(room_number, rooms):
    if room_number not in rooms:
        rooms[room_number] = room_number + 1
        return room_number
    empty = findEmptyRoom(rooms[room_number], rooms)
    rooms[room_number] = empty + 1
    return empty

def solution(k, room_numbers):
    answer = []
    rooms = {}
    for room_number in room_numbers:
        answer.append(findEmptyRoom(room_number, rooms))
    return answer
