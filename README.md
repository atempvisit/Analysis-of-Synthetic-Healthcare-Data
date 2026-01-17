# Analysis of Synthetic Healthcare Data (2018–2024)

**STAT112: Introduction to Data Processing and Visualization**  
Department of Statistics, Middle East Technical University  

**Instructor:** Prof. Dr. Ceylan Yozgatligil  
**Date:** January 16, 2026  

---

## Authors

- Md Mashroor Zilan Snigdho  
- Abdurrahman Melih Gökdağ  
- Mohamed Moustafa Mohamed Sharaki  
- Ömer Bilgiç  
- Şina Topaloğlu  

---

## Project Overview

This project analyzes a **synthetic healthcare dataset from Türkiye (2018–2024)** to explore demographic, clinical, and economic patterns in patient data. The goal is to identify observable trends across regions, diagnosis groups, and patient characteristics using Python-based data processing and visualization techniques.

---

## Dataset Description

The dataset contains patient-level healthcare records from multiple regions of Türkiye.

### Numeric Variables

- Patient ID  
- Age  
- BMI (kg/m²)  
- Systolic Blood Pressure  
- Cholesterol (mg/dL)  
- Length of Stay (Days)  
- Total Cost (TRY)  
- Year  
- Comorbidity Score  
- Readmitted within 30 Days (Binary)

### Categorical Variables

- Gender  
- Region  
- Insurance Type  
- Admission Type  
- Diagnosis Group  
- Discharge Status  

---

## Data Tidying and Cleaning

The following preprocessing steps were performed:

- Imported data using `pandas.read_csv()`
- Fixed separator issues using `sep=','`
- Inspected data using `.head()` and `.tail()`
- Corrected text inconsistencies using:
  - `str.strip()`
  - `str.lower()`
  - `str.replace()`
  - `str.title()`
- Renamed columns using `.rename()`
- Removed duplicate records using `.drop_duplicates()`
- Verified uniqueness with `.unique()`
- Converted the `Year` column to integer
- Corrected data types using `.astype()`
- Checked value ranges and confirmed no outliers
- Checked missing values using `.isnull().sum()`
- Handled missing values by dropping or imputing with mean, median, or mode

---

## Exploratory Data Analysis

### RQ1: How does the number of patients by gender vary across regions?

**Visualization:** Stacked Bar Chart  

- Marmara region has the highest total number of patients.
- Southern Anatolia has the lowest patient count.
- Gender distribution is generally balanced across regions.

---

### RQ2: Which diagnosis groups show the highest readmission density?

**Visualization:** Grouped Bar Chart by Age Group  

- Orthopedics shows high readmission rates, especially in the 70+ age group.
- Neurological conditions have the highest single readmission rate in the <30 age group.
- Oncology shows consistently high readmission risk across age groups.

---

### RQ3: Among cardiology patients, what is the relationship between BMI and systolic blood pressure?

**Visualization:** Scatter Plot with Regression Line  

- A positive linear relationship exists between BMI and systolic blood pressure.
- Most cardiology patients cluster within the BMI range of 22–28.

---

### RQ4: How does length of stay differ by insurance type for different admission types?

**Visualization:** Grouped Violin Plot  

- Median length of stay is approximately 5 days.
- Elective admissions have shorter hospital stays.
- Emergency and urgent admissions show the highest variability.
- Uninsured patients rarely experience long hospital stays.

---

### RQ5: How does length of stay affect total cost across diagnosis groups?

**Visualization:** Aggregated Line Chart  

- Total healthcare cost increases with length of stay.
- Oncology remains the most expensive diagnosis group.
- Infectious Disease costs increase rapidly with longer stays.
- Length of stay is a primary driver of total healthcare cost.

---

## Conclusion

- Marmara region has the highest patient admissions.
- Orthopedic patients show higher readmission rates.
- BMI and systolic blood pressure exhibit a positive linear relationship.
- Average hospital stay is approximately 5 days.
- Healthcare costs increase with length of stay, with oncology patients incurring the highest costs.
- Older patients are more likely to require hospitalization.

---

## Tools and Technologies

- **Python**
- **Pandas**
- **Seaborn**
- **Matplotlib**

---

## Reference

1. Synthetic Healthcare Dataset (2018–2024)

---

