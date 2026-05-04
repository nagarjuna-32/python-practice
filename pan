df["Revenue_norm"] = (df["Revenue"] - df["Revenue"].min()) / (df["Revenue"].max() - df["Revenue"].min())
