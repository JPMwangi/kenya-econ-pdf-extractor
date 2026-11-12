# 🇰🇪 Kenya Economic Data Pipeline: PDF to Structured Insights

> Automating the extraction of macroeconomic indicators from unstructured public PDF reports (KNBS, CBK, World Bank) to power data-driven journalism and economic research for **KenyaEconomicBriefs**.

---

## 🚀 Why This Matters (Organizational & Business Value)

In modern organizations, mountains of critical insights are trapped inside unstructured, static PDF reports. Manual copy-pasting is slow, error-prone, and unscalable. Building an automated extraction pipeline yields massive returns:

### **Organizational Benefits**
* **Elimination of Human Error:** Removes manual transcription mistakes when copying complex multi-column tables.
* **Speed to Insight:** Cuts data collection time from hours of manual labor to seconds of Python execution.
* **Scalability:** Easily handles hundreds of pages across recurring quarterly reports (GDP releases, inflation updates, monetary policy statements).
* **Reproducibility:** Creates a standardized, auditable trail from raw public document to final analysis.

### **Tangible Business & Analytical Outcomes**
* **Accelerated Content Velocity:** Enables rapid data turnaround for publishing timely insights on **KenyaEconomicBriefs**.
* **Data-Driven Credibility:** Backs macroeconomic arguments with precise, verifiable figures directly parsed from primary sources.
* **Operational Cost Savings:** Frees up high-value analytical hours from manual data wrangling to focus purely on strategic storytelling and economic forecasting.

---

## 🛠️ Tech Stack & Architecture

* **Core Engine:** [`pdfplumber`](https://github.com/jsvine/pdfplumber) for precise layout-aware text and grid extraction.
* **Data Wrangling:** [`pandas`](https://pandas.pydata.org/) for data cleaning, aggregation, and transformation.
* **Export Formats:** CSV and Excel (`openpyxl`) for downstream analysis and charting.

---

## 📂 Repository Structure

```text
kenya-econ-pdf-extractor/
│
├── data/
│   ├── raw/                  # Store downloaded public PDF reports here (ignored by git)
│   └── processed/            # Cleaned CSVs and Excel sheets ready for analysis
│
├── notebooks/
│   └── exploratory_parser.ipynb # Jupyter notebook for testing extraction on new layouts
│
├── src/
│   ├── __init__.py
│   ├── extractor.py          # Core table and regex extraction logic
│   └── cleaner.py            # Data sanitization, currency stripping, and formatting
│
├── .gitignore
├── requirements.txt
├── LICENSE
└── README.md
