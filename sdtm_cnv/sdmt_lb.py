import pandas as pd
import os


# folder path

folder_path = r"C:\\Users\\Vishnu\Desktop\\Clinical mapping\\sdtm_data"
file_name = "sdtm_lb.csv"
full_path = os.path.join(folder_path, file_name)

# raw lab data

raw_lb = pd.read_csv("raw_data\\raw_lb.csv")

# create SDTM LB dataset

sdtm_lb = raw_lb.copy()

# Add SDTM standard variables
sdtm_lb["STUDYID"] = "ABC123"
sdtm_lb["DOMAIN"] = "LB"

# Arrange SDTM variable order 
sdtm_lb = sdtm_lb[
    ["STUDYID", "DOMAIN","USUBJID","VISIT","LBTEST","LBSTRESN","LBSTRESU"]
]

# Sort per SDTM rules
sdtm_lb = sdtm_lb.sort_values(["USUBJID","VISIT"])

#save SDDTM LB dataset
sdtm_lb.to_csv(full_path, index = False)

print("SDTM LB dataset created !")
print(sdtm_lb.head())
