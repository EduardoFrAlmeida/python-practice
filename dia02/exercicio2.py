# find-second-maximum-number-in-a-list

n = int(input())
arr = map(int, input().split())
    
unique_scores = sorted(list(set(arr)))
    

print(unique_scores[-2])