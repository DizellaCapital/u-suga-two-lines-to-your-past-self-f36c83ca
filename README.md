# Two Lines to Your Past Self

[![make.fun · u-suga-two-lines-to-your-past-self-f36c83ca](https://make.fun/badge/u-suga-two-lines-to-your-past-self-f36c83ca.svg)](https://make.fun/bounty/u-suga-two-lines-to-your-past-self-f36c83ca?utm_source=github&utm_medium=readme&utm_campaign=u-suga-two-lines-to-your-past-self-f36c83ca)
[![rank](https://make.fun/badge/u-suga-two-lines-to-your-past-self-f36c83ca/DizellaCapital/u-suga-two-lines-to-your-past-self-f36c83ca/rank.svg)](https://make.fun/bounty/u-suga-two-lines-to-your-past-self-f36c83ca/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-suga-two-lines-to-your-past-self-f36c83ca)
[![reward](https://make.fun/badge/u-suga-two-lines-to-your-past-self-f36c83ca/DizellaCapital/u-suga-two-lines-to-your-past-self-f36c83ca/reward.svg)](https://make.fun/bounty/u-suga-two-lines-to-your-past-self-f36c83ca?utm_source=github&utm_medium=readme&utm_campaign=u-suga-two-lines-to-your-past-self-f36c83ca)

Two lines warning my past self about one specific moment — a [make.fun](https://make.fun) bounty entry by [@dizellacapital](https://make.fun/r/qxacafna).

## The two lines

> At 03:14 on Tuesday, don't merge Dedi's pull request before you run the migration on staging.
>
> That merge locked the database for six hours, and the client watched a frozen screen instead of our launch demo.

206 characters. Line 1 warns my past self about a single concrete moment — 03:14 on Tuesday, Dedi's pull request, the migration on staging. Line 2 traces the cause and effect: that merge locked the database for six hours, so the client watched a frozen screen instead of our launch demo.

## Run it

```sh
python3 main.py  # writes entry.txt to $MAKEFUN_OUTPUT_DIR (fallback /output)
```

`main.py` (stdlib only) validates the entry is exactly two lines, one sentence each, of 1–280 characters, writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` (fallback `/output`), then reads it back to verify the write.
