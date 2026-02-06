import pandas as pd
import os

folder_path = r"C:\\Users\\Vishnu\Desktop\\Clinical mapping\build_adsl"
file_name = "adsl.csv"
full_path = os.path.join(folder_path,file_name)

sdtm_dm = pd.read_csv("sdtm_data\sdtm_dm.csv")

adsl = sdtm_dm.copy()

# Derive age group 
adsl["AGEGRP"] = pd.cut(
    adsl["AGE"],
    bins = [0, 18, 40, 65, 120],
    labels = ["<18", "18-40", "41-65", ">65"]
)
# safety Population Flag , based on treatment exposure

adsl["SAFFL"] = "Y"

#Intent- to - Treat Flag

adsl["ITTFL"] = "Y"

# Planned Treatment (for training)

adsl["TRT01P"] = "Drug A"

# Keep ADaM standard order
adsl = adsl[
    [
        "STUDYID",
        "USUBJID",
        "SUBJID",
        "AGE",
        "AGEGRP",
        "SEX",
        "COUNTRY",
        "SAFFL",
        "ITTFL",
        "TRT01P"
    ]
]

# Sort (ADaM rule)
adsl.sort_values("USUBJID")

# Save ADSL
adsl.to_csv(full_path, index=False)

print("ADSL dataset Created !")
print(adsl.head(10))