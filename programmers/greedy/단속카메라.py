def solution(routes):
    camera_cnt = 1
    routes.sort()
    camera_loc = routes.pop(0)[1]
    for route in routes:
        if route[0] <= camera_loc:
            camera_loc = min(camera_loc, route[1])
        elif route[0] > camera_loc:
            camera_loc = route[1]
            camera_cnt += 1
    return camera_cnt

# print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]]	))
