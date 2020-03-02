import sys

card_n = int(sys.stdin.readline())
card_list = sys.stdin.readline().split()
cards = [int(i) for i in card_list]

test_n = int(sys.stdin.readline())
test_list = sys.stdin.readline().split()
tests = [int(i) for i in test_list]

def solution(cards, tests):
    cards = sorted(cards)
    
    for i in tests:
        print(binary_search(cards, i), end = ' ')
        
    

def binary_search(list, target):
    s = 0 
    e = len(list) - 1 
    while s <= e:
        mid = (s+e) // 2
        if list[mid] > target:
            e = mid - 1
        elif list[mid] < target:
            s = mid + 1
        else:
            e = s = mid
            count = 1
            while s-1 >= 0 and list[s-1] == target:
                s -= 1
                count += 1
            while e+1 <= len(list) - 1 and list[e+1] == target:
                e += 1
                count += 1 
            return count
    return 0
                
    
solution(cards, tests)