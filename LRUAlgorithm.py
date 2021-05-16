from collections import deque

if __name__ == '__main__':


    def solution(cities, cacheSize):

        answer = 0
        cache = []
        for city in cities:
            city = city.lower()
            if city in cache:
                answer += 1
                # 이건 뭐?
                # if len(cache) >= cacheSize:
                # 갱신
                cache.remove(city)
                cache.append(city)
                #?
                # else:
                # cache.append(city)

            else:
                answer += 5
                if cacheSize != 0:
                    # cacheSize 보다 길수는 없다. 있으면 갱신하고 없으면 채우도록 짠다면
                    if len(cache) == cacheSize:
                        # 삭제
                        cache.pop(0)
                    cache.append(city)


        return answer

    assert solution(["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"],3) , solution(["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"],3)

    # solution 1 (가장 쓰이지 않은 요소가 리스트의 첫 번째 요소 )









