# IRRBB-Duration-Gap-Management-Tool

## Objective
This project implements a leverage-adjusted **Duration Gap framework** to quantify the impact of interest rate movements on a bank’s **Economic Value of Equity (EVE)**. The model is aligned with **FRM and IRRBB methodology** and demonstrates how duration mismatches between assets and liabilities translate into changes in net worth under interest rate shocks.

## Methodology
- Market-value weighted duration calculation for assets and liabilities
- Computation of leverage-adjusted duration gap
- Scenario-based estimation of change in Economic Value of Equity (ΔEVE)
- Interpretation of interest rate risk exposure (long vs short duration equity)

## Model Overview
The model follows these steps:
1. Construct asset and liability duration profiles using market values
2. Compute average asset duration (DA) and liability duration (DL)
3. Calculate the leverage-adjusted duration gap
4. Apply a user-defined interest rate shock
5. Estimate the resulting change in market value of equity (ΔEVE)
6. Provide management-style interpretation of results

## How to Run
1. Ensure Python 3.x is installed on your system.
2. Install the required dependency: pandas
3. Download the repository and navigate to the project folder.
4. Run the script.
5. When prompted, enter the interest rate change in percentage points (e.g., -3 for +3%).
6. Review the asset and liability duration tables, duration gap summary, and ΔEVE impact printed in the console.

## Key Insights
- A positive duration gap indicates equity behaves like a **long-duration position**, losing value when interest rates rise.
- A negative duration gap indicates equity behaves like a **short-duration position**, gaining value when interest rates rise.
- The magnitude of the duration gap determines the sensitivity of equity to interest rate movements.

## Tools Used
- Python
- Pandas

## Disclaimer
This is a simplified educational model developed for learning and demonstration purposes. It does not represent a production-ready risk system.

