# part 1

```
1 · 1 2 · · · · · · ·
· · · · · · · · · · ·
· · · · · · · · · · ·
· · · · · · 1 1 · 1 1
1 · 1 · · · · · · · ·
· · · · · · · · · 1 ·
· · · · · · · 1 · · ·
```

```
  0 1 2 3 4 5 6 7 8 9 0
0 1 · 1 2 · · · · · · ·
1 · · · · · · · · · · ·
2 · · · · · · · · · · ·
3 · · · · · · 1 1 · 1 1
4 1 · 1 · · · · · · · ·
5 · · · · · · · · · 1 ·
6 · · · · · · · 1 · · ·
```

1 - 3 = 5

# part 2

        if Da % D == 0 and Db % D == 0:
            a = Da // D
            b = Db // D
            price = 3*a + b
            coins += price
            print(a, b, price)
        else:
            print(f"Machine has no winners {machine}")