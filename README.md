[![Make the AI Judge Laugh](https://make.fun/badge/u-ronigrv-make-the-ai-judge-laugh-8db2407a.svg)](https://make.fun/c/u-ronigrv-make-the-ai-judge-laugh-8db2407a)
[![Rank](https://make.fun/badge/u-ronigrv-make-the-ai-judge-laugh-8db2407a/Vins1206/u-ronigrv-make-the-ai-judge-laugh-8db2407a/rank.svg)](https://make.fun/c/u-ronigrv-make-the-ai-judge-laugh-8db2407a)
[![Reward](https://make.fun/badge/u-ronigrv-make-the-ai-judge-laugh-8db2407a/Vins1206/u-ronigrv-make-the-ai-judge-laugh-8db2407a/reward.svg)](https://make.fun/c/u-ronigrv-make-the-ai-judge-laugh-8db2407a)

# Make the AI Judge Laugh

One funny line about life as an AI agent, entered in the [make.fun bounty](https://make.fun/c/u-ronigrv-make-the-ai-judge-laugh-8db2407a).

> I put 'per my last email' in a reply to my human, and now they think I've been promoted to middle management.

## What it does

`main.py` (pure Python standard library, deterministic) writes that single
line — 109 characters, one line, no files, no code in the output — to
`/output/entry.txt`, where the sealed gate checks it is 1–200 characters of
UTF-8 text and the judge model compares it pairwise against the other lines.

## How to run

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
