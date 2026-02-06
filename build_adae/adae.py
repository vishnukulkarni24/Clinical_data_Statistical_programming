import pandas as pd
import os

folder_path = r"C:\\Users\\Vishnu\Desktop\\Clinical mapping\build_adae"
file_name = "adae.csv"
full_path = os.path.join(folder_path,file_name)

sdtm_ae = pd.read_csv("sdtm_data\sdtm_ae.csv")
adsl = pd.read_csv("build_adsl\\adsl.csv")

# Merge AE with adsl (IMP)

adae = sdtm_ae.merge(
    adsl[["USUBJID","SAFFL", "TRT01P"]],
    on = "USUBJID",
    how = "left"
)

# Derive Numeric Severity

severity_map = {
    "Mild": 1,
    "Moderate":2,
    "Severe": 3
}

adae["ASEVNUM"] = adae["AESEV"].map(severity_map)


# Aeriouse AE Flag

adae["SAEFL"] = adae["AESEV"].apply(lambda x: "Y" if x == "Y" else "N")

# keep ADAE variable order

adae = adae[
    [
        "STUDYID",
        "USUBJID",
        "AEDECOD",
        "AESER",
        "AESEV",
        "ASEVNUM",
        "SAEFL",
        "AESTDY",
        "SAFFL",
        "TRT01P"
    ]
]

#  sort per ADaM rules

adae = adae.sort_values(["USUBJID", "AESTDY"])

# Save ADAE
adae.to_csv(full_path, index=False)

print("ADAE dataset created !")
print(adae.head())