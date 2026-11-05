# Plugin CLI

A tiny, beginner-friendly Python command-line tool that runs **plugins**.
Each plugin is a single `.py` file that fetches some data (a price, a quote, the weather...) and returns it as a dictionary. The CLI finds every plugin in the `plugins/` folder, runs them all, and prints the results.

If one plugin crashes, the others keep running.

## What it does

```
$ python main.py
        example_coingecko
┏━━━━━━━━━━━━━┳━━━━━━━━━━━━━┓
┃ Key         ┃ Value       ┃
┡━━━━━━━━━━━━━╇━━━━━━━━━━━━━┩
│ Coin        │ Bitcoin     │
│ Price (USD) │ $67,000.00  │
└─────────────┴─────────────┘

Done: 1 plugin(s) succeeded, 0 failed.
```

## Install

You need Python 3.8+.

```bash
pip install -r requirements.txt
```

Only `requests` is required. `rich` is optional and just makes the output prettier; without it the CLI prints plain text.

```bash
pip install requests
```

## Run

```bash
python main.py
```

## Write your own plugin

A plugin is one file in `plugins/` with one function:

```python
def fetch_data():
    return {"Some label": "some value"}
```

Copy `plugins/example_coingecko.py`, change the API, and you're done. See [CONTRIBUTING.md](CONTRIBUTING.md) for the full step-by-step guide.

## Plugin ideas for contributors

Pick one and open a Pull Request!

- 🌦️ Weather for a city (Open-Meteo, no API key)
- 💱 Currency exchange rates (Frankfurter API)
- 🪙 Ethereum / other crypto prices (CoinGecko)
- 🛰️ Current position of the ISS (Open Notify)
- 🐙 GitHub repo stars and open issues
- 📰 Top Hacker News story
- 💬 Random quote of the day
- 🌍 Your public IP and approximate location
- 🚀 Next SpaceX launch
- 🐱 Random cat fact
- 📦 Latest version of a PyPI or npm package
- 🌅 Sunrise and sunset times

Prefer free APIs that need **no API key**.

## License

MIT. Use it, change it, share it.
