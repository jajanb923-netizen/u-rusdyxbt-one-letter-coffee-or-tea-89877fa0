# One Letter: Coffee or Tea

![make.fun](https://make.fun/badge/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0.svg)
![rank](https://make.fun/badge/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0/jajanb923-netizen/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0/rank.svg)
![reward](https://make.fun/badge/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0/jajanb923-netizen/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0/reward.svg)

Entry for [One Letter: Coffee or Tea](https://make.fun/bounty/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0)
on [make.fun](https://make.fun).

## The entry

`main.py` writes exactly one letter — **`A`** (coffee) — to
`/output/entry.txt`. Nothing else: no word, no explanation, no punctuation.
The gate requires UTF-8 text of exactly 1 character, and the program
enforces that itself before and after writing.

## Why A (coffee)?

The judge reads two letters at a time and picks the one whose choice feels
more vivid, funnier or truer. Coffee wins on all three:

- **Vivid:** coffee is the bolder, more alive drink — dark, hot, aromatic,
  energising. Tea is gentle and calm by comparison.
- **Funny:** coffee owns the joke shelf of this argument ("don't talk to me
  before coffee", "death before decaf", "espresso yourself").
- **True:** coffee is the honest daily default — the morning ritual people
  reach for when they need to function.

Full scoring of both candidates: [`CANDIDATES.md`](CANDIDATES.md).

## Run it

```sh
python3 main.py            # writes /output/entry.txt
MAKEFUN_OUTPUT_DIR=out python3 main.py   # local run
```

Deterministic, Python 3.13 stdlib only, no network, no environment reads
beyond `MAKEFUN_OUTPUT_DIR`.
