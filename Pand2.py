q1 = df["Revenue"].quantile(0.25)
q3 = df["Revenue"].quantile(0.75)
iqr = q3 - q1

outliers = df[(df["Revenue"] < q1 - 1.5*iqr) | (df["Revenue"] > q3 + 1.5*iqr)]
print(outliers)
