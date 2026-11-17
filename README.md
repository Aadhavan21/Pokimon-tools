# POKEMON TOOLS

A free, mobile-friendly web application powered by **Python 3 in the browser via Pyodide**, designed for Android Chrome and static hosting on **GitHub Pages**.

## Features

### 1. Random Pokemon Picker – Route 1
- Includes the 10 first-stage regional bird Pokemon (Generations 1–9):
  - **Gen 1:** Pidgey (#16), Spearow (#21)
  - **Gen 2:** Hoothoot (#163)
  - **Gen 3:** Taillow (#276)
  - **Gen 4:** Starly (#396)
  - **Gen 5:** Pidove (#519)
  - **Gen 6:** Fletchling (#661)
  - **Gen 7:** Pikipek (#731)
  - **Gen 8:** Rookidee (#821)
  - **Gen 9:** Wattrel (#940)
- Uses Python's cryptographically secure `secrets.randbelow(10)` so every Pokemon has an exact **10%** selection chance.
- Smooth right-to-left decelerating horizontal roulette animation with official 2D PokeAPI artwork and hidden names until the roulette stops.

### 2. Pokemon Damage Calculator
- Implements the Generation 3 damage formula directly in Python (`damage_calculator.py`).
- Supports **Pokemon Level (L)**, **Move Power (P)**, **Attack / Special Attack (A)**, **Defense / Special Defense (D)**, **STAB** (`1.5x` / `1x`), **Type Effectiveness** (`2x`, `1x`, `0.5x`, `0.25x`), and **Critical Hit** (`2x` / `1x`).
- Runs **1,000 random damage rolls** (`85%` to `100%`) in Python and displays Minimum, Average, and Maximum damage.

## Project Structure

```text
pokemon-tools/
├── index.html
├── pokemon_picker.py
├── damage_calculator.py
└── README.md
```

## Deploying to GitHub Pages

1. Extract `pokemon-tools.zip`.
2. Upload `index.html`, `pokemon_picker.py`, `damage_calculator.py`, and `README.md` to the root of your GitHub repository.
3. Go to **Settings → Pages** in your repository.
4. Under **Build and deployment**, set **Source** to **Deploy from a branch**, choose your `main` branch and `/ (root)` folder, and click **Save**.
5. Open your GitHub Pages URL in Google Chrome on Android or desktop.

> **Note:** Because `index.html` loads `pokemon_picker.py` and `damage_calculator.py` using `fetch()`, open the site via GitHub Pages or a local HTTP server (`python -m http.server`) rather than `file://`. An internet connection is required to load Pyodide and official Pokemon artwork.
