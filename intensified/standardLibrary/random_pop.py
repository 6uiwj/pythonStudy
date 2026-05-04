import random
#리스트의 요소 중 무작위로 하나를 선택해 꺼내 그 값을 리턴
# def random_pop(data):
#     number = random.randint(0, len(data) - 1)
#     return data.pop(number)

def random_pop(data):
    number = random.choice(data) #random.choice : 입력으로 받은 리스트에서 무작위로 하나를 선택하여 리턴
    data.remove(number)
    return number

if __name__ == "__main__":
    data = [1,2,3,4,5]
    while data:
        print(random_pop(data))

data = [1,2,3,4,5]
print(random.sample(data, len(data))) #리스트의 항목을 무작위로 섞고 싶을 때