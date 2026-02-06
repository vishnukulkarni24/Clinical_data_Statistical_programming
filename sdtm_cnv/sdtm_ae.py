import pandas as pd
import os


# folder path
folder_path = r"C:\\Users\\Vishnu\Desktop\\Clinical mapping\\sdtm_data"
file_name = "sdtm_ae.csv"
full_path = os.path.join(folder_path, file_name)

# raw dataset path

raw_ae = pd.read_csv(r"raw_data\\raw_ae.csv")

# Create SDTM AE dataset
sdtm_ae = raw_ae.copy()

# Add required SDTM variables
sdtm_ae["STUDYID"] = "ABC123"
sdtm_ae["DOMAIN"] = "AE"

# Ensure correct column naming 

sdtm_ae = sdtm_ae.rename(columns={
    "AEDECOD" : "AEDECOD",
    "AESER" : "AESER",
    "AESEV" : "AESEV",
    "AESTDY" : "AESTDY"
})


# Arrange SDTM variable order
sdtm_ae = sdtm_ae[
    ["STUDYID", "DOMAIN", "USUBJID", "AEDECOD", "AESER", "AESEV", "AESTDY"]
]

# sort per SDTM rules

sdtm_ae = sdtm_ae.sort_values(["USUBJID", "AESTDY"])

# save SDTM AE dataset

sdtm_ae.to_csv(full_path, index = False)

print("SDTM AE dataset created.")
print(sdtm_ae.head(10))