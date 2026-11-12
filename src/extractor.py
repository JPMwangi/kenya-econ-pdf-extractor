"""Core PDF Data Extraction Module for KenyaEconomicBriefs."""

import os
import pandas as pd
import pdfplumber


def clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:
  """Applies mandatory data cleaning rules to the extracted DataFrame."""
  df.dropna(how="all", inplace=True)
  df.dropna(axis=1, how="all", inplace=True)
  df = df.map(lambda x: x.strip() if isinstance(x, str) else x)
  df.replace(["-", "N/A", "n/a", ""], pd.NA, inplace=True)
  return df


def extract_tables_from_pdf(pdf_path: str, output_path: str):
  print(f"[*] Processing document: {pdf_path}")
  all_tables = []

  try:
    with pdfplumber.open(pdf_path) as pdf:
      for page in pdf.pages:
        tables = page.extract_tables()
        for table in tables:
          if table and len(table) > 1:
            df = pd.DataFrame(table[1:], columns=table[0])
            all_tables.append(df)

    if all_tables:
      master_df = pd.concat(all_tables, ignore_index=True)
      master_df = clean_dataframe(master_df)

      os.makedirs(os.path.dirname(output_path), exist_ok=True)
      master_df.to_csv(output_path, index=False)
      print(f"[+] Success! Extracted data saved to {output_path}")
    else:
      print("[-] No valid tables found using grid extraction.")

  except Exception as e:
    print(f"[!] Error processing PDF: {e}")


if __name__ == "__main__":
  # Example local test run
  print("PDF Extractor module loaded successfully.")
