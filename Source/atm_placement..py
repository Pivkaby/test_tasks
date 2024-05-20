def can_place_atms(L, max_distance, k):
    count = 0
    for distance in L:
        count += (distance - 1) // max_distance
        if count > k:
            return False
    return True

def binary_search(L, k):
    left, right = 1, max(L)
    while left < right:
        mid = (left + right) // 2
        if can_place_atms(L, mid, k):
            right = mid
        else:
            left = mid + 1
    return left

def distribute_atms(L, max_distance):
    new_L = []
    for distance in L:
        parts = (distance + max_distance - 1) // max_distance
        equal_part = distance // parts
        remainder = distance % parts
        for _ in range(parts - 1):
            new_L.append(equal_part)
        new_L.append(equal_part + remainder)
    return new_L

def add_atms(k, L):
    max_distance = binary_search(L, k)
    return distribute_atms(L, max_distance)

# n = 5
# k = 4
# L = [100, 180, 50, 45, 150]

n = int(input())
k = int(input())
L = []
for _ in range(n):
    distance = int(input())
    L.append(distance)

new_distances = add_atms(k, L)
print(new_distances)