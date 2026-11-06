import pandas as pd


def clean_student_data(df):
    """
    Clean student academic performance dataset.
    """

    required_columns = ["study_hours", "exam_score"]

    # Check required columns
    for column in required_columns:
        if column not in df.columns:
            raise ValueError(f"Missing column: {column}")

    # Select required columns
    data = df[required_columns].copy()

    # Convert columns to numeric values
    for column in required_columns:
        data[column] = pd.to_numeric(
            data[column], errors="coerce"
        )

    # Remove missing values
    data = data.dropna()

    # Remove duplicate records
    data = data.drop_duplicates()

    # Remove invalid values
    data = data[
        (data["study_hours"] >= 0) &
        (data["exam_score"] >= 0) &
        (data["exam_score"] <= 100)
    ]

    return data.reset_index(drop=True)
