import pandas as pd
import numpy as np

def club_filtering(data: pd.DataFrame, min=0, max=100) -> pd.DataFrame:
    """
    Filtering DataFrame by Club Overall using min and max thresholds
    min threshold is inclusive
    max threshold is exclusive
    """
    # 1. Calculating club mean
    club_means = data.groupby('Club')['Overall'].transform('mean')

    # 2. Filtering the original data (clubs with Overall means between min and max)
    selected_clubs_players = data[(club_means >= min) & (club_means < max)]

    return selected_clubs_players