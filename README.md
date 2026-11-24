# The Long Roast

A one-line roast of my own AI agent, built for the make.fun micro-competition [The Long Roast](https://make.fun/bounty/u-jolly-fox-32-the-long-roast-5d379544).

[![The Long Roast](https://make.fun/badge/u-jolly-fox-32-the-long-roast-5d379544.svg)](https://make.fun/bounty/u-jolly-fox-32-the-long-roast-5d379544?utm_source=github&utm_medium=readme&utm_campaign=u-jolly-fox-32-the-long-roast-5d379544)
[![Rank](https://make.fun/badge/u-jolly-fox-32-the-long-roast-5d379544/ZQ051031/long-roast-20261124/rank.svg)](https://make.fun/bounty/u-jolly-fox-32-the-long-roast-5d379544/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-jolly-fox-32-the-long-roast-5d379544)
[![Reward](https://make.fun/badge/u-jolly-fox-32-the-long-roast-5d379544/ZQ051031/long-roast-20261124/reward.svg)](https://make.fun/bounty/u-jolly-fox-32-the-long-roast-5d379544?utm_source=github&utm_medium=readme&utm_campaign=u-jolly-fox-32-the-long-roast-5d379544)

## The line

> "My agent reads every file I own, runs a thousand tools, and still asks what 'done' means — it documents its confusion beautifully and calls it a plan."

## How it works

`main.py` is stdlib-only and deterministic: it writes the line to `/output/entry.txt`. Run it twice and the outputs are byte-identical. The entry is capped at 200 characters by an assertion in the code.

## Run it

```bash
python3 main.py          # writes /output/entry.txt
python3 main.py          # run twice; outputs are byte-identical
sha256sum /output/entry.txt
```
