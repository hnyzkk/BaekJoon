# 문제
# 수직선 위에 N개의 좌표 X1, X2, ..., XN이 있다. 이 좌표에 좌표 압축을 적용하려고 한다.
# Xi를 좌표 압축한 결과 X'i의 값은 Xi > Xj를 만족하는 서로 다른 좌표 Xj의 개수와 같아야 한다.
# X1, X2, ..., XN에 좌표 압축을 적용한 결과 X'1, X'2, ..., X'N를 출력해보자.

# 입력
# 첫째 줄에 N이 주어진다.
# 둘째 줄에는 공백 한 칸으로 구분된 X1, X2, ..., XN이 주어진다.

# 출력
# 첫째 줄에 X'1, X'2, ..., X'N을 공백 한 칸으로 구분해서 출력한다.

# 제한
# 1 ≤ N ≤ 1,000,000
# -109 ≤ Xi ≤ 109

import sys
# 좌표 개수 입력
n = int(sys.stdin.readline())
# 좌표 입력
nums = list(map(int, sys.stdin.readline().split()))
# 중복 제거한 정렬된 배열 생성
sorted_nums = sorted(list(set(nums)))
# 값 접근 속도를 높이기 위해 딕셔너리로 값:인덱스 순서로 딕셔너리 생성
nums_dict = {value:index for index, value in enumerate(sorted_nums)}
# 원래 배열의 값들을 키로 하는 딕셔너리 값으로 전환
for i in range(len(nums)):
    nums[i] = nums_dict[nums[i]]
# 결과값 출력
for i in nums:
    print(i)
