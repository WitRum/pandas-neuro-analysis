# pandas-neuro-analysis

A small, self-contained pandas pipeline for loading, cleaning, summarizing and plotting tabular data. It is a scaffold for exploratory data analysis (EDA) that can be pointed at other datasets, such as neuroscience measurements.

The demo runs on a public sample CSV of 200 people's heights and weights, which stands in for real neuro data.

## What it does

1. **Load** a CSV straight from a URL into a DataFrame
2. **Clean** it by dropping rows with missing values and filtering out unrealistic outliers
3. **Describe** it with summary statistics and a null-value check
4. **Plot** a scatter chart and save it as `height_vs_weight.png`

## Quick start

```bash
git clone https://github.com/WitRum/pandas-neuro-analysis.git
cd pandas-neuro-analysis
pip install -r requirements.txt
python neuro_data.py
```

## Adapting it to your own data

- Change the URL in `load_data()` to your own CSV or file path
- Update the column names and thresholds in `clean_data()` and `plot_data()`

## Tech

Python 3, pandas, matplotlib
