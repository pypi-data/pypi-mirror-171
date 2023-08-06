# shanten-tools

Fast calculation of shanten numbers in Japanese Mahjong.

## Usage

```
>>> from shanten_tools import shanten
>>> import numpy as np
>>> hand = np.array([
>>>     3,1,1,1,1,1,1,1,3,
>>>     0,0,0,0,0,0,0,0,0,
>>>     0,0,0,0,0,0,0,0,0,
>>>     0,0,0,0,0,0,0], dtype=np.uint8)
>>> shanten(hand)
1
>>> hand = np.array([
>>>     3,1,1,1,1,1,1,1,3,
>>>     0,0,0,0,0,0,0,0,0,
>>>     0,0,0,0,0,0,0,0,0,
>>>     0,0,0,0,0,0,1], dtype=np.uint8)
>>> shanten_discard(hand)
array([2,1,2,2,1,2,2,1,2,
       0,0,0,0,0,0,0,0,0,
       0,0,0,0,0,0,0,0,0,
       0,0,0,0,0,0,1], dtype=uint64)
```

## Notes
- shanten number **+1** is output