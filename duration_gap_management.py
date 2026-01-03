import pandas as pd

# Asset data
asset_data = {
    "Asset Type": ["US Treasuries", "Commercial Loans", "Municipal Bonds"],
    "Market Value": [400, 120, 230],
    "Duration": [5.45, 2.34, 1.23]
}

assets_df = pd.DataFrame(asset_data,index=None)
print("ASSETS DATA")

total_assets = assets_df["Market Value"].sum()
print("\nTotal Assets:", total_assets)

assets_df["Weight"] = (assets_df["Market Value"] / total_assets).round(4)
print(assets_df)

assets_df["Weighted Duration"] = assets_df["Weight"] * assets_df["Duration"]

DA = assets_df["Weighted Duration"].sum()
print("\nAverage Duration of Assets (DA):", round(DA, 3))

print("\n------------------------------------------------------------")

# Liability data
liability_data = {
    "Liability Type": ["Negotiable CDs", "Other Time Deposits", "Subordinated Notes"],
    "Market Value": [200, 120, 100],
    "Duration": [3.45, 2.56, 1.54]
}

liabilities_df = pd.DataFrame(liability_data)
print("\nLIABILITIES DATA")

total_liabilities = liabilities_df["Market Value"].sum()
print("\nTotal Liabilities:", total_liabilities)

liabilities_df["Weight"] = (liabilities_df["Market Value"] / total_liabilities).round(4)
print("\nLIABILITIES WITH WEIGHTS")
print(liabilities_df)

liabilities_df["Weighted Duration"] = liabilities_df["Weight"] * liabilities_df["Duration"]

DL = liabilities_df["Weighted Duration"].sum()
print("\nAverage Duration of Liabilities (DL):", round(DL, 3))

# Duration Gap Calculation
duration_gap = DA - (DL * (total_liabilities / total_assets))
print("\n------------------------------------------------------------")
print("\nDURATION GAP SUMMARY")
print("\n------------------------------------------------------------")
print(f"Total Assets (A)               : {total_assets:.2f}")
print(f"Total Liabilities (L)          : {total_liabilities:.2f}")
print(f"Average Asset Duration         : {DA:.3f} years")
print(f"Average Liability Duration     : {DL:.3f} years")
print(f"Leverage-Adjusted Duration Gap : {duration_gap:.3f} years")
print("------------------------------------------------------------")

user_rate_change = float(
    input("\nEnter interest rate change in percentage points (e.g. -3 for +3%): ")
)
delta_y = user_rate_change / 100

initial_rate = 0.07  # 7%

delta_eve = -duration_gap * total_assets * (delta_y / (1 + initial_rate))

direction = "increase" if delta_y > 0 else "decrease"

print("\n------------------------------------------------------------")
print("\nECONOMIC VALUE OF EQUITY (EVE) IMPACT")
print("\n------------------------------------------------------------")
print(f"Interest Rate Shock Applied : {user_rate_change:+.2f}%")
print(f"Initial Interest Rate       : {initial_rate*100:.2f}%")
print(f"Change in Market Value of Equity (ΔEVE): {delta_eve:.3f} million")
print("------------------------------------------------------------")



# Example link : https://analystprep.com/study-notes/frm/risk-management-for-changing-interest-rates-asset-liability-management-and-duration-techniques/





