import pandas as pd

# Read SDTM LB and ADSL
sdtm_lb = pd.read_csv("sdtm_data\sdtm_lb.csv")
adsl = pd.read_csv("build_adsl\\adsl.csv")

# Merge LB with ADSL
adlb = sdtm_lb.merge(
    adsl[["USUBJID", "SAFFL", "TRT01P"]],
    on="USUBJID",
    how="left"
)

#  Identify baseline value
# Baseline = VISIT == 'Baseline'
baseline = (
    adlb[adlb["VISIT"] == "Baseline"]
    .groupby(["USUBJID", "LBTEST"])["LBSTRESN"]
    .first()
    .reset_index()
    .rename(columns={"LBSTRESN": "BASE"})
)

# Merge baseline back
adlb = adlb.merge(
    baseline,
    on=["USUBJID", "LBTEST"],
    how="left"
)

# Change from baseline
adlb["CHG"] = adlb["LBSTRESN"] - adlb["BASE"]

# Keep ADLB variable order
adlb = adlb[
    [
        "STUDYID",
        "USUBJID",
        "LBTEST",
        "VISIT",
        "LBSTRESN",
        "BASE",
        "CHG",
        "SAFFL",
        "TRT01P"
    ]
]

# Sort per ADaM rules
adlb = adlb.sort_values(["USUBJID", "LBTEST", "VISIT"])

# Save ADLB
adlb.to_csv("adlb.csv", index=False)


print("ADLB dataset created!")
print(adlb.head())
