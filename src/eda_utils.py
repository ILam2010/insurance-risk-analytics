def calculate_loss_ratio(df):
    return df["TotalClaims"] / df["TotalPremium"]