import pandas as pd
import os 

# folder path
folder_path = r"C:\\Users\\Vishnu\Desktop\\Clinical mapping\\sdtm_data"
file_name = "sdtm_dm.csv"
full_path = os.path.join(folder_path, file_name)

# raw data
raw_dm = pd.read_csv(r"raw_data\\raw_dm.csv")


# Create SDTM Structure

sdtm_dm = raw_dm.copy()

# add SDTM Standard Variables

sdtm_dm["STUDYID"] = "ABC123"
sdtm_dm["DOMAIN"] = "DM"

# Create unique subject ID 
sdtm_dm["USUBJID"] = sdtm_dm["STUDYID"] + "-" \
    + sdtm_dm["SUBJID"].astype(str)

# keep SDTM order

sdtm_dm = sdtm_dm[
    ["STUDYID", "DOMAIN", "USUBJID", "SUBJID", "AGE", "SEX", "COUNTRY"]
]

# Sort (SDTM rule)

sdtm_dm = sdtm_dm.sort_values("USUBJID")

# Save SDTM dataset

sdtm_dm.to_csv(full_path, index= False)

print("SDTM DM dataset Created !")
print(sdtm_dm.head())