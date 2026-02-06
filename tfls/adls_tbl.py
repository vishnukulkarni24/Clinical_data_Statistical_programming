import pandas as pd


adsl = pd.read_csv("build_adsl\\adsl.csv")

# Subject count
subject_count = adsl["USUBJID"].nunique()

# Age summary
age_summary = adsl["AGE"].agg(["mean", "min", "max"]).round(1)

# Sex distribution
sex_dist = adsl["SEX"].value_counts().reset_index()
sex_dist.columns = ["SEX", "COUNT"]

# Age group distribution
agegrp_dist = adsl["AGEGRP"].value_counts().reset_index()
agegrp_dist.columns = ["AGEGRP", "COUNT"]

demographic_summary = {
    "Total Subjects": subject_count,
    "Age Summary": age_summary,
    "Sex Distribution": sex_dist,
    "Age Group Distribution": agegrp_dist
}

print("Demographic Summary Generated")


adae = pd.read_csv("build_adae\\adae.csv")

# AE frequency by term
ae_freq = (
    adae.groupby("AEDECOD")
    .size()
    .reset_index(name="EVENT_COUNT")
    .sort_values("EVENT_COUNT", ascending=False)
)

# AE severity summary
ae_severity = (
    adae.groupby(["AEDECOD", "AESEV"])
    .size()
    .reset_index(name="COUNT")
)

# Serious AE count
sae_summary = adae["SAEFL"].value_counts().reset_index()
sae_summary.columns = ["SAEFL", "COUNT"]

print("AE Frequency Tables Generated")

adlb = pd.read_csv("build_adlb\\adlb.csv")

# Mean lab values by visit
lab_visit_summary = (
    adlb.groupby("VISIT")["LBSTRESN"]
    .mean()
    .reset_index(name="MEAN_LAB_VALUE")
    .round(2)
)

# Mean change from baseline by visit
lab_change_summary = (
    adlb.groupby("VISIT")["CHG"]
    .mean()
    .reset_index(name="MEAN_CHANGE_FROM_BASELINE")
    .round(2)
)

print("Lab Shift Tables Generated")


with pd.ExcelWriter("clinical_TFLs.xlsx") as writer:

    # Demographics
    age_summary.to_frame(name="VALUE").to_excel(writer, sheet_name="Age_Summary")
    sex_dist.to_excel(writer, sheet_name="Sex_Distribution", index=False)
    agegrp_dist.to_excel(writer, sheet_name="Age_Group_Distribution", index=False)

    # AE Tables
    ae_freq.to_excel(writer, sheet_name="AE_Frequency", index=False)
    ae_severity.to_excel(writer, sheet_name="AE_Severity", index=False)
    sae_summary.to_excel(writer, sheet_name="Serious_AE", index=False)

    # Lab Tables
    lab_visit_summary.to_excel(writer, sheet_name="Lab_By_Visit", index=False)
    lab_change_summary.to_excel(writer, sheet_name="Lab_Change", index=False)

print("Submission-style Excel file created: clinical_TFLs.xlsx")