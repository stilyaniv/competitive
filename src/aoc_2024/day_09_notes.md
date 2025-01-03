# example

```
disk_map    2333133121414131402
disk_map    2 3  3  3  1 3  3  1 2  1 4   1 4   1 3  1 4   0 2 0
file_id     0    1     2    3    4    5     6     7    8     9
padded      00...111...2 ...333. 44 . 5555. 6666. 777. 8888  99
arranged    0 0 9 9 8 1 1 1 8 8 8  2  7  7  7  3  3  3  6  4  4  6  5  5  5  5  6  6
block_pos   0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
checksum    0
```

# full input

```
5    4   7      0 7      9        6     6     27 97 68 84 26 92 7 4 9 1 ...
0        1        2               3           4  5  6  7  8  9  10  11
00000....1111111  2222222.........333333......
```

## end of padded line

```
print(line[-8:])
print(padded_line[-20:])

6                             1   4                    3               3
9997                              9998                                 9999
9997,9997,9997,9997,9997,9997,'.',9998,9998,9998,9998, '.', '.', '.', '9999', '9999', '9999']
```

## start of padded line

```
print(padded_line[:25])
['0', '0', '0', '0', '0', '.', '.', '.', '.', '1', '1', '1', '1', '1', '1', '1', '2', '2', '2', '2', '2', '2', '2', '.', '.']

print(padded_line[-25:])
['9', '8', '9', '9', '9', '8', '9', '9', '9', '8', '.', '.', '.', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9']
```

# part 2

```
2333133121414131402

2 3 1 3 2 4 4 3 4 2

 3 3 3 1 1 1 1 1 0

||||
                                       |||
012345678901234567890123456789012345678901
00...111...2...333.44.5555.6666.777.888899
0099.111...2...333.44.5555.6666.777.8888..
0099.1117772...333.44.5555.6666.....8888..
0099.111777244.333....5555.6666.....8888..
00992111777.44.333....5555.6666.....8888..
```

```
00...111...2...333.44.5555.6666.777.888899
  99....
```

l = [0,0] + 5*['.'] + 4 * [10] + ['.'] + 3 \* [11]

len(l) == 15

empty_start = 2
empty_end = 7

file_start = 12
file_end = 15

l[empty_start:empty_start+file_size], l[file_start:file_end] = l[file_start:file_end], l[empty_start:empty_start+file_size]

```
input
[0, 0, '.', '.', '.', '.', '.', 10, 10, 10, 10, '.', 11, 11, 11]
output
[0, 0, 11,  11,  11, '.', '.', 10, 10, 10, 10, '.', '.', '.', '.']
```

# part 2 - alt approach

```
0 1 2 3 4 5 6 7 8 9

2333133121414131402

2 3 1 3 2 4 4 3 4 2

 3 3 3 1 1 1 1 1 0
```
