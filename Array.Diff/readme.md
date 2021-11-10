---
Tags:
    - Arrays
    - Fundamentals
    - Algorithms
---

DESCRIPTION:

Your goal is this kata is to implement a difference function, which subtracts one list from another and returns the result.

It should remove all values from `a`, which are present in list `b` keeping their order


```
array_diff([1,2],[1]) == [2]
```

If a value is present in `b`, all of its occurences must be removed from the other:

```
array_diff([1,2,2,2,3],[2]) == [1,3]
```
