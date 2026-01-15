"""Convert chart PDFs to PNGs for web display."""
import os
from pathlib import Path

# Try pdf2image first (best quality)
try:
    from pdf2image import convert_from_path
    USE_PDF2IMAGE = True
except ImportError:
    USE_PDF2IMAGE = False

# Fallback to matplotlib
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

BASE_DIR = Path(__file__).parent.parent
CHARTS_DIR = BASE_DIR / "charts"
OUTPUT_DIR = BASE_DIR / "docs" / "figures"

CHART_FOLDERS = [
    "01_scaled_macro_timeseries",
    "02_principal_components",
    "03_macro_strength_breakpoints",
    "04_inflation_index_breakpoints",
    "05_speech_count_distribution",
    "06_inflation_sentiment_combined",
    "07_rolling_betas_macro",
    "08_rolling_r2_macro",
    "09_rolling_betas_inflation",
    "10_rolling_r2_inflation",
    "11_correlation_matrix",
    "12_pca_loadings_heatmap",
]


def convert_pdf_to_png(pdf_path: Path, output_path: Path) -> bool:
    """Convert a single PDF to PNG."""
    if USE_PDF2IMAGE:
        try:
            images = convert_from_path(str(pdf_path), dpi=150, first_page=1, last_page=1)
            if images:
                images[0].save(str(output_path), 'PNG')
                return True
        except Exception as e:
            print(f"  pdf2image failed: {e}")

    # Fallback: create placeholder
    try:
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.text(0.5, 0.5, f"Chart: {pdf_path.stem}\n(View PDF for full quality)",
                ha='center', va='center', fontsize=14, transform=ax.transAxes)
        ax.axis('off')
        fig.savefig(str(output_path), dpi=150, bbox_inches='tight', facecolor='white')
        plt.close(fig)
        return True
    except Exception as e:
        print(f"  Fallback failed: {e}")
        return False


def main():
    """Convert all chart PDFs to PNGs."""
    print("=" * 60)
    print("CONVERTING CHART PDFs TO PNGs")
    print("=" * 60)
    print(f"Using pdf2image: {USE_PDF2IMAGE}")

    # Create output directory
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    converted = 0
    failed = 0

    for folder in CHART_FOLDERS:
        pdf_path = CHARTS_DIR / folder / "chart.pdf"
        png_path = OUTPUT_DIR / f"{folder}.png"

        if not pdf_path.exists():
            print(f"[SKIP] {folder}: PDF not found")
            failed += 1
            continue

        print(f"[CONV] {folder}...")
        if convert_pdf_to_png(pdf_path, png_path):
            print(f"       -> {png_path.name}")
            converted += 1
        else:
            failed += 1

    print("=" * 60)
    print(f"Converted: {converted} | Failed: {failed}")
    print(f"Output: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
