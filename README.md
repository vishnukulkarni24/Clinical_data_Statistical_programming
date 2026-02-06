# Clinical Statistical Programming – End-to-End Workflow (Python)

This repository demonstrates my **regular hands-on practice in Statistical Programming**, following industry-standard clinical trial workflows used in pharmaceutical and CRO environments.

The project simulates a **real-world clinical study pipeline**, covering data preparation, analysis dataset creation, and generation of analysis tables (TFLs).

---

## Project Overview

The objective of this project is to replicate **end-to-end clinical data processing** typically performed by a Statistical Programmer:

- Convert raw clinical data into **CDISC SDTM domains**
- Build **ADaM analysis datasets**
- Perform required **derivations**
- Generate **TFLs (Tables)** for statistical review
- Produce **submission-style Excel outputs**

All steps follow **CDISC principles** and **regulatory expectations**, implemented using Python to mirror SAS-based workflows.

---

##  Project Structure

clinical-statistical-programming/
├── raw_data/
│   ├── raw_dm.csv        # Raw demographics
│   ├── raw_ae.csv        # Raw adverse events
│   └── raw_lb.csv        # Raw lab data
│
├── sdtm/
│   ├── sdtm_dm.csv       # SDTM DM domain
│   ├── sdtm_ae.csv       # SDTM AE domain
│   └── sdtm_lb.csv       # SDTM LB domain
│
├── adam/
│   ├── adsl.csv          # Subject-level analysis dataset
│   ├── adae.csv          # Adverse events analysis dataset
│   └── adlb.csv          # Lab analysis dataset
│
├── tfl/
│   └── clinical_TFLs.xlsx # Submission-style analysis tables
│
└── README.md




