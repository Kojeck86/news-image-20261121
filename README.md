# THE WORLD — front page of 21 November 2026

[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/Kojeck86/news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/Kojeck86/news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

A one-image summary of the world's news of Saturday 21 November 2026, drawn as a newspaper front page. Built for the make.fun bounty [news-image-20261121](https://make.fun/bounty/news-image-20261121).

## Stories

- **Missiles fall on Poland** — Russia fires 400+ drones and 110 missiles at Ukraine overnight; two missiles land in Poland.
- **AI rout drags markets into correction** — S&P 500 −3.7%, Nasdaq −5.3%, wiping out all of 2026's gains.
- **Myanmar guilty of genocide** — the World Court holds a state responsible for the first time.
- **Biggest UK–EU deal since Brexit** — three pacts: food trade, carbon markets, youth mobility.
- **Climate talks run past deadline** — COP31 in Antalya in overtime over fossil fuels.
- Also: Riyadh intercepts Houthi missiles; cancer pill hope (tumours vanish in 1 in 12); Peru quake 6.9.

Sources: BBC, Al Jazeera, Financial Times, Guardian, OneTurn — 21 November 2026.

## How it works

`draw_frontpage.py` draws the front page (PIL, DejaVu fonts) into `entry.png` (1024×1024, under 1 MiB). `main.py` (Python 3.13, standard library only) copies `entry.png` to `/output/entry.png` — deterministic, no network.
