# part 1

```
    00 01 02 03 04 05 06 07 08 09
00   R  R  R  R  I  I  C  C  F  F
01   R  R  R  R  I  I  C  C  C  F
02   V  V  R  R  R  C  C  F  F  F
03   V  V  R  C  C  C  J  F  F  F
04   V  V  V  V  C  J  J  C  F  E
05   V  V  I  V  C  C  J  J  E  E
06   V  V  I  I  I  C  J  J  E  E
07   M  I  I  I  I  I  J  J  E  E
08   M  I  I  I  S  I  J  E  E  E
09   M  M  M  I  S  S  J  E  E  E
```

# part 2

```
A A A A A A
A A A B B A
A A A B B A
A B B A A A
A B B A A A
A A A A A A
```

A: 4 outside, 8 inside
B: each has 4 outside

```
if we use █ to represent out-of-bounds squares
    -1  0  1  2  3  4  5  6  7  8  9
-1   #  #  #  #  #  #  #  #  #  #  #
 0   #  R  R  R  R  I  I  C  C  F  F
 1   #  R  R  R  R  I  I  C  C  C  F
 2   #  V  V  R  R  R  C  C  F  F  F
 3   #  V  V  R  C  C  C  J  F  F  F
 4   #  V  V  V  V  C  J  J  C  F  E
 5   #  V  V  I  V  C  C  J  J  E  E
 6   #  V  V  I  I  I  C  J  J  E  E
 7   #  M  I  I  I  I  I  J  J  E  E
 8   #  M  I  I  I  S  I  J  E  E  E
 9   #  M  M  M  I  S  S  J  E  E  E
```

```
for R the single unit perimeters with method from part 1 are:
15 visible, 3 overlapping at corners 3,3 and 1,2 and 4,1
    -1  0  1  2  3  4  5
-1      #  #  #  #
 0   #  R  R  R  R  #
 1   #  R  R  R  R  #
 2      #  #  R  R  R  #
 3         #  R  #  #
 4            #

 part 2 counts these as 10 fences

if we don't count duplicates and the middle from sequential portions
     -1  0  1  2  3  4  5
-1       #  #  #  #
 0    #  R  R  R  R  #
 1    #  R  R  R  R  #
 2       #  #  R  R  R  #
 3          #  R  #  #
 4             #
15 - 5

perims = sorted(perim, key=lambda t: (t[0], t[1]))
[(-1, 0),
(-1, 1),
(0, -1),
(0, 2),
(1, -1),
(1, 2),
(1, 2),
(1, 3),
(2, -1),
(2, 4),
(3, -1),
(3, 3),
(3, 3),
(4, 0),
(4, 1),
(4, 1),
(4, 3),
(5, 2)]
```

![alt text](image.png)
option 1)
considering the right-most R, it should count fence above but not below
the one below has been counted towards the **parent** node - so pass parent node
to allow for checking whether the parent's already counted
for R @ 4,2: 1) parent is R @ 3,2 2) check direction of parent - which one of x or y stayed the same 3) if direction is left or right then check the paren't up and down nodes for perimeter -> but doesn't this mean every other node will reset

option 2)
return list of boundaries and then re-process them to identify same lines

```
min_perims = []
for i in range(len(perims)):
    total_diff = perims[i+1][0] - perims[i][0], perims[i+1][1] - perims[i][1]
    print((perims[i][0],perims[i][1]))
    print(f"\t{total_diff}")


(-1, 0)     1   
	(0, 1)
(-1, 1)     1
	(1, -2)
(0, -1)     2
	(0, 3)
(0, 2)      3
	(1, -3)
(1, -1)     4
	(0, 3)
(1, 2)      5
	(0, 0)
(1, 2)      5
	(0, 1)
(1, 3)      5
	(1, -4)
(2, -1)     6
	(0, 5)
(2, 4)      7
	(1, -5)
(3, -1)     8
	(0, 4)
(3, 3)      9
	(0, 0)
(3, 3)      9
	(1, -3)
(4, 0)      10
	(0, 1)
(4, 1)      10
	(0, 0)
(4, 1)      10
	(0, 2)
(4, 3)      11
	(1, -1)
(5, 2)      12
```

```
-1, 0
-1, 1
0, -1
0, 2
1, -1
1, 2
1, 2
1, 3
2, -1
2, 4
3, -1
3, 3
3, 3
4, 0
4, 1
4, 1
4, 3
5, 2
```

```
min_perims = []
for i in range(len(perims)):
    total_diff = abs(perims[i][0] - perims[i+1][0]) + abs(perims[i][1] - perims[i+1][1])
    print(total_diff)
```
