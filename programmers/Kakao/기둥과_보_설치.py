def is_validate(building):
    for build_frame in building:
        x, y = build_frame[0], build_frame[1]
        if build_frame[2] == 0:
            if y != 0 and [x, y, 1] not in building and [x-1, y, 1] not in building and [x, y-1, 0] not in building:
                return False
        else:
            if [x,y-1,0] not in building and [x+1,y-1,0] not in building and ([x-1,y,1] not in building or [x+1,y,1] not in building):
                return False
    return True

def can_install(build_frame, building):
    x, y = build_frame[0], build_frame[1]
    if build_frame[2] == 0:
        if y == 0 or [x, y, 1] in building or [x-1, y, 1] in building or [x, y-1, 0] in building:
            return True
    else:
        if [x, y-1, 0] in building or [x+1, y-1, 0] in building or ([x-1, y, 1] in building and [x+1, y, 1] in building):
            return True
    return False
    
def solution(n, build_frames):
    building = []
    for build_frame in build_frames:
        if build_frame[3] == 0:
            if build_frame[:-1] in building:
                building.remove(build_frame[:-1])
                if not is_validate(building):
                    building.append(build_frame[:-1])
        else:
            if can_install(build_frame, building):
                building.append(build_frame[:-1])
    building = sorted(building, key=lambda x : x)
    return building
