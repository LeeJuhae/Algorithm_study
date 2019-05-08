# Chap1. 알고리즘의 소개

### 02 이진 탐색

리스트의 원소들이 정렬되어 있을 때 사용할 수 있다.

```python
def binary_search(elements, item):
    low = 0
    high = len(elements)-1
    while low <= high:
        mid = (low+high)//2
        if item == elements[mid]:
            return mid
        elif item < elements[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return None 
```

단순 탐색의 경우에는 O(n)의 실행 시간으로 실행되지만 , 이진 탐색의 경우에는 O(log n)으로 실행된다.



### 03 빅오 표기법

__리스트의 크기가 증가할 때 알고리즘의 실행 시간이 어떻게 증가하는지 파악__해야 한다. 따라서 **빅오 표기법**을 사용한다.

빅오 표기법은 알고리즘의 실행 시간을 속도를 시간 단위로 세지 않고, 연산 횟수로 나타내는 방법이다. 또한 최악의 경우에 대한 실행 시간을 의미한다. 

- 대표적인 5가지의 실행 시간 비교 

  : O(log n) < O(n) < O(n log n) < O(n^2) < O(n!)

