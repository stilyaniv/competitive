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

     0  0  0  0  1  1  2  2  3  3
     0  0  0  0  1  1  2  2  2  3
     4  4  0  0  0  5  5  3  3  3
     4  4  0  7  7  7  8  3  3  3
     4  4  4  4  7  9  9 10  3 11
     4  4 12  4  7  7  9  9 13 13
     4  4 12 12 12  7  9  9 13 13
    14 15 15 15 15 15  9  9 13 13
    14 15 15 15 16 15  9 17 17 17
    14 14 14 15 16 16  9 17 17 17
```

# part 2

A A A A A A
A A A B B A
A A A B B A
A B B A A A
A B B A A A
A A A A A A

A: 4 outside, 8 inside
B: each has 4 outside

![alt text](image.png)
considering the right-most R, it should count fence above but not below
the one below has been counted towards the **parent** node - so pass parent node
to allow for checking whether the parent's already counted
for R @ 4,2: 1) parent is R @ 3,2 2) check direction of parent - which one of x or y stayed the same 3) if direction is left or right then check the paren't up and down nodes for perimeter -> but doesn't this mean every other node will reset 
