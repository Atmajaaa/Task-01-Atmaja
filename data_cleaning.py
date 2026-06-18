import pandas as pd

df = pd.read_excel("Online-Store-Orders.xlsx")

print("========== DATASET INFO ==========")
print(df.info())

print("\n========== DATASET SHAPE ==========")
print(df.shape)

print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

print("\n========== DUPLICATE ROWS ==========")
print(df.duplicated().sum())

print("\n========== DATA TYPES ==========")
print(df.dtypes)

df["CouponCode"] = df["CouponCode"].fillna("No Coupon")

print("Remaining Missing Values:")
print(df.isnull().sum())

df.to_excel("Cleaned_Dataset.xlsx", index=False)

print("\nDataset cleaned successfully!")
print("Cleaned file saved as Cleaned_Dataset.xlsx")