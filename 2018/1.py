import time

def part1():
    return sum([int(line) for line in open('1.in')])   

# 1.2
#found = 0
#total = 0
#seen = {0 : 1}
#freqs = [line.strip() for line in sys.stdin]
#while(not(found)):
#    for line in freqs:
#        if line.strip():
#            total += int(line.strip())
#            if total in seen:
#                print("Seen again:", total)
#                found = 1
#                break
#            else:
#                seen[total] = 1
#if not(found):
#    print("No repeats")
t0 = time.time()
print(part1())
t1 = time.time()
print(t1 - t0)

