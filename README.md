# jump to python study

# 🐍 Python 데이터 타입 정리

## 1. 기본 타입 (Primitive-like)

### int (정수)
- 정수 값 저장
- 크기 제한 없음
- immutable (불변)

```python
a = 10
```

---

### float (실수)
- 소수점 포함 숫자
- immutable
- 정밀도 문제 존재

```python
print(0.1 + 0.2)  # 0.30000000000000004
```

---

### bool (불리언)
- True / False
- 조건문에서 사용

```python
flag = True
```

---

### str (문자열)
- 문자열 데이터
- immutable (불변)

```python
s = "hello"
s = s + " world"
```

---

## 2. 컬렉션 타입 (Collection)

## list
- 순서 O
- 중복 O
- mutable (가변)

```python
arr = [1, 2, 3]
arr[0] = 10
```

### ✔️ 대표 함수

| 함수 | 설명 |
|------|------|
| append(x) | 요소 추가 |
| extend(iterable) | 여러 요소 추가 |
| insert(i, x) | 특정 위치에 추가 |
| remove(x) | 값 제거 |
| pop([i]) | 인덱스로 제거 |
| sort() | 정렬 |
| reverse() | 뒤집기 |
| index(x) | 위치 찾기 |
| count(x) | 개수 세기 |

---

### ✔️ 예시

```python
arr = [1, 2, 3]

arr.append(4)        # [1,2,3,4]
arr.insert(1, 10)    # [1,10,2,3,4]
arr.remove(2)        # [1,10,3,4]
arr.pop()            # [1,10,3]
arr.sort()           # 정렬
```




---

## tuple
- 순서 O
- immutable (불변)

```python
t = (1, 2, 3)
```


### ✔️ 대표 함수

| 함수 | 설명 |
|------|------|
| count(x) | 개수 |
| index(x) | 위치 |

---

### ✔️ 예시

```python
t = (1, 2, 3, 1)

t.count(1)   # 2
t.index(2)   # 1
```



---

## set
- 중복 X
- 순서 X
- mutable

```python
s = {1, 2, 3}
```

### ✔️ 대표 함수

| 함수 | 설명 |
|------|------|
| add(x) | 요소 추가 |
| remove(x) | 요소 제거 |
| discard(x) | 없으면 무시 |
| union(s) | 합집합 |
| intersection(s) | 교집합 |
| difference(s) | 차집합 |

---

### ✔️ 예시

```python
a = {1, 2, 3}
b = {3, 4, 5}

a.add(10)                  # {1,2,3,10}
a.remove(2)                # {1,3,10}
a.union(b)                 # {1,2,3,4,5}
a.intersection(b)          # {3}
```



---

## dict
- key-value 구조
- mutable
- JSON과 동일 구조

```python
user = {"name": "넙치", "age": 20}
```

### ✔️ 대표 함수

| 함수 | 설명 |
|------|------|
| get(key) | 값 조회 (안전) |
| keys() | key 목록 |
| values() | value 목록 |
| items() | key-value 쌍 |
| update() | 값 수정 |
| pop(key) | 삭제 |
| clear() | 전체 삭제 |

---

### ✔️ 예시

```python
user = {"name": "넙치", "age": 20}

user.get("name")       # 넙치
user["age"] = 30       # 수정
user.update({"city":"서울"})
user.pop("age")        # 삭제
```


---

## 3. None 타입

### None
- 값 없음 (null 개념)

```python
a = None
```

---

## 4. 핵심 개념

### Mutable vs Immutable

- immutable: int, float, str, tuple
- mutable: list, dict, set

---

### 불변 객체 예시

```python
a = 10
b = a
a = 20

print(b)  # 10
```

---

### 가변 객체 예시

```python
a = [1, 2, 3]
b = a
a[0] = 100

print(b)  # [100, 2, 3]
```

---

## 5. 참조(Reference)

- 변수는 값을 저장하는 게 아니라 객체를 참조함

```python
a = [1, 2, 3]
b = a
```

---

## 6. 사용 기준

- list → 데이터 목록
- dict → JSON / API 응답 (핵심)
- set → 중복 제거
- tuple → 변경 불가 데이터
- str → 불변이라 성능 고려 필요

---
