n = input()
half = len(n) // 2
head, tail = n[:half], n[half:]
if sum(int(x) for x in head) == sum(int(x) for x in tail):
    print("LUCKY")
else:
    print("READY")