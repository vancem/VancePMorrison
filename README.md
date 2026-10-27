# VancePMorrison

Home page for Vance Morrison (VancePMorrison).

**The published page: <https://vancem.github.io/VancePMorrison/>**

The words live in [index.md](index.md). A small build turns that file into static HTML. There is no table of contents and no print view.

## Rebuild locally

```
pip install -r requirements.txt
python build.py
```

`python build.py` writes the compiled page to `site/`. Open `site/index.html` in a browser. The `site/` folder is not committed. It is only the output of the build.

## What happens on GitHub

A push to `main` runs the `Deploy site` GitHub Action. That action runs the same build and publishes the result to GitHub Pages, so the HTML is regenerated from `index.md` on every update. The compiled site is not stored in the repository. It is served at <https://vancem.github.io/VancePMorrison/>.

GitHub Pages has to be set to **Source: GitHub Actions** (Settings → Pages) for that address to update.
