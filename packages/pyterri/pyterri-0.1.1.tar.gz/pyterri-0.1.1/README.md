# pyterri
A simple python package for getting [territorial.io](https://territorial.io) player and clan data

*Still in early development*

## Installing
`pip install pyterri`

## Usage
Currently only one function (getClans()) is provided (although more are on the way).
The below example gets data for every listed clan.

```py
from pyterri import clan

print(clan.getClans())
```

You can also pass a limit like so:

```py
from pyterri import clan

print(clan.getClans(limit = 10))
```

This will list the top 10 clans.