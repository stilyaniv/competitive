# Part 2

```
stones = splitr(stones, 35)

raw 49.4273
  lru_cache(maxsize=128) 11.2277
  lru_cache(maxsize=256) 3.2114
  lru_cache(maxsize=512) 0.6988

stones = splitr(stones, 40)
  lru_cache(maxsize=512) 5.0176
  lru_cache(maxsize=4096) 4.8837

stones = splitr(stones, 75)
  lru_cache(maxsize=512) crashes
  @cached(cache={}, key=lambda stones, blinks: hashkey(stones))  # 3.8626

final_size = splitr(stones, 75)
  @cached(cache={}, key=lambda stones, blinks: hashkey(stones))
    - wrong value, number of blinks needs to be part of cache when counting instead of returning the full item
  lru_cache(maxsize=512) 28.0527 sec = 6330486168

```

final_size = splitr(stones, 75)
@lru_cache(maxsize=512) slow
@lru_cache(maxsize=8192) 7.1464s
