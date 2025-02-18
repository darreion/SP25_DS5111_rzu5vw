import pytest
import pandas as pd
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from bin.normalize_csv import normalize_csv


def test_normalize_csv():

    test_input = "tests/sample_raw.csv"
    test_output = "tests/sample_raw_norm.csv"

    raw_data = pd.DataFrame({
        "Symbol": ["AAPL", "GOOG"],
        "Price": [150.25, 2800.75],
        "Change": [1.50, -12.25],
        "% Change": [1.01, -0.44]
    })
    raw_data.to_csv(test_input, index=False)

    output_file = normalize_csv(test_input)

    assert os.path.exists(output_file)

    df = pd.read_csv(output_file)

    expected_columns = ["symbol", "price", "price_change", "price_percent_change"]
    assert list(df.columns) == expected_columns

    os.remove(test_input)
    os.remove(test_output)


if __name__ == "__main__":
    pytest.main()
