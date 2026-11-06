import pandas as pd
from scipy.stats import pearsonr


def analyze_data(df):
    """
    Analyze the relationship between study hours and exam scores.
    """

    required_columns = ["study_hours", "exam_score"]

    for column in required_columns:
        if column not in df.columns:
            raise ValueError(f"Missing required column: {column}")

    # Select required columns
    data = df[required_columns].copy()

    # Remove missing values
    data = data.dropna()

    # Exclude invalid records
    data = data[
        (data["study_hours"] >= 0) &
        (data["exam_score"] >= 0) &
        (data["exam_score"] <= 100)
    ]

    if len(data) < 3:
        raise ValueError("At least 3 valid records are required.")

    # Descriptive statistics
    summary = data.describe().to_dict()

    # Pearson correlation
    correlation, p_value = pearsonr(
        data["study_hours"],
        data["exam_score"]
    )

    return {
        "sample_size": len(data),
        "summary": summary,
        "correlation": float(correlation),
        "p_value": float(p_value),
        "significant": bool(p_value < 0.05)
    }
