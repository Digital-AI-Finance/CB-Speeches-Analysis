# CB Speeches Analysis

[![CI](https://github.com/Digital-AI-Finance/CB-Speeches-Analysis/actions/workflows/ci.yml/badge.svg)](https://github.com/Digital-AI-Finance/CB-Speeches-Analysis/actions/workflows/ci.yml)
[![Deploy](https://github.com/Digital-AI-Finance/CB-Speeches-Analysis/actions/workflows/deploy.yml/badge.svg)](https://github.com/Digital-AI-Finance/CB-Speeches-Analysis/actions/workflows/deploy.yml)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Analyzing the relationship between Federal Reserve speech sentiment and macroeconomic conditions using PCA, structural break detection, and rolling regression.**

## Key Finding

> **Near-zero correlation (0.005)** between CB speech sentiment (hawkish/dovish) and macroeconomic indices - a significant empirical result challenging assumptions about central bank communication effectiveness.

| Metric | Value |
|--------|-------|
| Macro-Hawkish Correlation | 0.005 |
| Variance Explained (2 PCs) | 72% |
| US Fed Speeches Analyzed | 2,421 |
| Time Period | 1996-2025 |

## Quick Start

```bash
# Clone
git clone https://github.com/Digital-AI-Finance/CB-Speeches-Analysis.git
cd CB-Speeches-Analysis

# Install
pip install -r requirements.txt

# Run analysis
python -c "from analysis.run_all import run_pipeline; run_pipeline(use_cached=True, verbose=True)"

# Generate charts
cd charts && python run_all_charts.py

# Launch dashboard
streamlit run app.py
```

## Project Structure

```
CB-Speeches-Analysis/
├── analysis/              # Core pipeline modules
│   ├── config.py          # Configuration and parameters
│   ├── run_all.py         # Master pipeline orchestrator
│   ├── data_loader.py     # FRED API / CSV loading
│   ├── preprocessing.py   # Rolling standardization
│   ├── pca_analysis.py    # PCA dimensionality reduction
│   ├── breakpoint_detection.py  # PELT algorithm
│   ├── speech_sentiment.py      # Sentiment aggregation
│   └── rolling_regression.py    # Rolling betas and R-squared
├── charts/                # 12 chart folders + utilities
│   ├── 01_scaled_macro_timeseries/
│   ├── 02_principal_components/
│   ├── ...
│   └── run_all_charts.py
├── data/                  # Input and output data
│   ├── gigando_speeches_ner_v2.parquet  # 20k+ CB speeches
│   ├── macroeconomic_data.csv           # FRED data
│   └── *.csv, *.json                    # Pipeline outputs
├── tests/                 # Unit tests
├── docs/                  # GitHub Pages website
├── app.py                 # Streamlit dashboard
├── generate_dashboard.py  # Static HTML generator
└── requirements.txt
```

## Analysis Pipeline

1. **Data Loading** - Load FRED macroeconomic data and CB speeches
2. **Preprocessing** - 12-month rolling standardization
3. **PCA Analysis** - Extract Macro Strength Index (PC1) and Inflation Index (PC2)
4. **Breakpoint Detection** - PELT algorithm identifies structural breaks
5. **Sentiment Aggregation** - Monthly hawkish/dovish counts from speeches
6. **Rolling Regression** - 36-month rolling betas and R-squared

## Data Sources

| Source | Description | Period |
|--------|-------------|--------|
| FRED | Fed Funds Rate, CPI, PPI, GDP, Unemployment, Nonfarm Payrolls | 1996-2025 |
| BIS/Gigando | 2,421 US Federal Reserve speeches with sentiment labels | 1996-2025 |

## Key Parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `ROLLING_WINDOW` | 12 | Months for standardization |
| `REGRESSION_WINDOW` | 36 | Months for rolling regression |
| `PELT_PENALTY` | 4 | Breakpoint detection sensitivity |
| `RANDOM_STATE` | 42 | Reproducibility seed |

## Output Files

| File | Description |
|------|-------------|
| `pca_components.csv` | PC1 (Macro Index), PC2 (Inflation Index) |
| `pca_loadings.csv` | Component weights on each macro variable |
| `breakpoints.json` | PELT-detected structural break dates |
| `sentiment_aggregated.csv` | Monthly hawkish/dovish counts |
| `correlation_matrix.csv` | First-difference correlations |

## Charts

12 publication-ready figures covering:
- Scaled macroeconomic time series
- Principal components over time
- Structural breakpoints (Macro and Inflation indices)
- Speech sentiment distribution
- Rolling regression results (betas, R-squared)
- Correlation matrix and PCA loadings heatmaps

## Running Tests

```bash
python -m pytest tests/ -v
```

## Documentation

- [Interactive Dashboard](https://digital-ai-finance.github.io/CB-Speeches-Analysis/dashboard.html)
- [Methodology](https://digital-ai-finance.github.io/CB-Speeches-Analysis/methodology/)
- [Reproduce Analysis](https://digital-ai-finance.github.io/CB-Speeches-Analysis/reproduce/)
- [All Figures](https://digital-ai-finance.github.io/CB-Speeches-Analysis/figures/)

## Citation

```bibtex
@article{taibi2025cbspeeches,
  title={Central Bank Communication and Macroeconomic Conditions:
         A PCA-Based Framework for Analyzing Narrative-Reality Disconnect},
  author={Taibi, Gabin and Osterrieder, Joerg},
  journal={Working Paper},
  year={2025},
  institution={University of Zurich}
}
```

## License

MIT License - see [LICENSE](LICENSE) for details.

## Acknowledgments

Part of the SNSF Narrative Digital Finance project (Grant IZCOZ0_213370).

## Links

- [Project Website](https://digital-ai-finance.github.io/CB-Speeches-Analysis/)
- [GitHub Repository](https://github.com/Digital-AI-Finance/CB-Speeches-Analysis)
- [Parent Project](https://digital-ai-finance.github.io/Narrative-Digital-Finance/)
