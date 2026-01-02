# 2차원 평면 위의 점 N개가 주어진다. 좌표를 x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.

# 첫째 줄에 점의 개수 N (1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N개의 줄에는 i번점의 위치 xi와 yi가 주어진다. (-100,000 ≤ xi, yi ≤ 100,000) 좌표는 항상 정수이고, 위치가 같은 두 점은 없다.

# 첫째 줄부터 N개의 줄에 점을 정렬한 결과를 출력한다.

DOT_COUNT_SIZE = 100000

num = []

# 좌표 개수 입력
while 1:
    dot_count = int(input(""))
    
    if dot_count >= 1 and dot_count <= DOT_COUNT_SIZE:
        break
    else:
        print("점의 개수 입력 범위가 잘못됐습니다. 다시 입력하세요.")
        continue
    
# 좌표 입력 및 2차원 리스트 추가
for i in range(1, dot_count+1):
    [num1, num2] = map(int, input().split())
    num.append([num1, num2])

# 결과값 출력
for i in sorted(num):
    print(f"{i[0]} {i[1]}")


