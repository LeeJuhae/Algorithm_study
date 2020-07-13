def solution(cacheSize, cities):
    answer = 0
    if cacheSize == 0:
        return 5 * len(cities)
    cache = []
    for city in cities:
        city = city.upper()
        if city in cache:
            cache.append(cache.pop(cache.index(city)))
            answer += 1
        else:
            cache.append(city)
            answer += 5
            if len(cache) > cacheSize:
                cache.pop(0)
    return answer
