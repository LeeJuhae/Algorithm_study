# Chap2. 선택 정렬

### 02 배열과 연결 리스트

여러 개의 항목을 저장할 때 배열 또는 리스트를 사용한다.

배열의 모든 항목은 이웃하는 위치에 저장되고, 리스트의 모든 항목은 흩어지지만 각 항목이 다음 항목의 주소를 저장한다.

|      | 배열 | 리스트 |
| :--: | :--: | :----: |
| 읽기 | O(1) |  O(n)  |
| 삽입 | O(n) |  O(1)  |
| 삭제 | O(n) |  O(1)  |

(※ O(1) : 고정 시간, O(n) : 선형 시간)

### 03 선택 정렬

모든 원소를 비교하여 최솟값을 찾아 제일 앞에 위치 시킨다.

```python
def findSmallest(arr):
	smallest = arr[0]
  for i in range(1,len(arr)):
    if arr[i] < smallest:
      smallest = arr[i]
  return arr.index(smallest)

def selectionSort(arr):
  result = []
  for i in range(len(arr)):
    result.append(arr.pop(findSmallest(arr))
  return result
```

최솟값을 찾기 위해 O(n) 의 실행 시간이 소요되며, 이 작업을 원소의 개수만큼 해야하므로 **선택 정렬의 시간 복잡도는 O(n^2)**이다.



