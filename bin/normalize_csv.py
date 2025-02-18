import pandas as pd
import sys
import os


def normalize_csv(input_filepath):
    assert os.path.exists(input_filepath), f"File not found: {input_filepath}"

    df = pd.read_csv(input_filepath)

    column_mappings = {
        "Symbol": "symbol",
        "Price": "price",
        "Change": "price_change",
        "% Change": "price_percent_change",
        "Ticker": "symbol",
        "Last Price": "price",
        "Change Amount": "price_change",
        "Change Percentage": "price_percent_change",
    }

    df.rename(columns=column_mappings, inplace=True)

    required_columns = ["symbol", "price", "price_change", "price_percent_change"]
    available_columns = [col for col in required_columns if col in df.columns]

    df = df[available_columns]

    output_filepath = f"{input_filepath.replace('.csv', '')}_norm.csv"
    df.to_csv(output_filepath, index=False)

    return output_filepath


if __name__ == "__main__":
    assert len(sys.argv) == 2, "Usage: python bin/normalize_csv.py <input_csv>"
    input_csv = sys.argv[1]
    normalized_csv = normalize_csv(input_csv)
    print(f"Normalized CSV created: {normalized_csv}")
