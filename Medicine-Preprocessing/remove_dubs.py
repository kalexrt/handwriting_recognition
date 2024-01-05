import pandas as pd

medicines = pd.read_csv("pharmacy.csv")["medicines"]

medicines.drop_duplicates(inplace=True)

medicines.to_csv("Pharmacy.csv", index=False)
