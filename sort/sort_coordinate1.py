# 2차원 평면 위의 점 N개가 주어진다. 좌표를 x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.

# 첫째 줄에 점의 개수 N (1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N개의 줄에는 i번점의 위치 xi와 yi가 주어진다. (-100,000 ≤ xi, yi ≤ 100,000) 좌표는 항상 정수이고, 위치가 같은 두 점은 없다.

# 첫째 줄부터 N개의 줄에 점을 정렬한 결과를 출력한다.

DOT_COUNT_SIZE = 100000
DOT_UNDER_SIZE = -100000
DOT_UPPER_SIZE = 100000

def counting_sort(origin):
    range_list = [0] * (max(origin) + 1)
    sorted_list = [0,] 
    
    for i in range_list:
        print(f"{i}")
    for i in range(0, len(origin)):
        range_list[origin[i]] += 1
    for i in range(0, len(range_list)):
        range_list[i+1] += range_list[i]
    for i in range(len(origin)-1, -1, -1):
        sorted_list[range_list[origin[i]]] = origin[i]
        range_list[origin[i]] -= 1
    return sorted_list

x = []
y = []

sorted_x = []
sorted_y = []

while 1:
    dot_count = int(input(""))
    
    if dot_count >= 1 and dot_count <= DOT_COUNT_SIZE:
        print(dot_count, type(dot_count))
    else:
        print("점의 개수 입력 범위가 잘못됐습니다. 다시 입력하세요.")
        continue
    break

for i in range(0, dot_count):
    num1, num2 = map(int, input().split())
    x.append(num1)
    y.append(num2)

for i in range(0, dot_count):
    print(f"저장된 좌표: {x[i]} {y[i]}")
    
sorted_x = counting_sort(x)
sorted_y = counting_sort(y)

for i in range(0, dot_count):
    print(f"정렬된 좌표: {sorted_x[i]} {sorted_y[i]}")


