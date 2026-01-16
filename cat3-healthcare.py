import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
# Make sure to update the path if your file location changes
df = pd.read_csv(r'c:\Users\ND_COMP_0300\Desktop\Group_11_Healthcare\synthetic_healthcare_1700_clean.csv')

# Set the visualization style
sns.set(style="whitegrid")

# Create the figure size
plt.figure(figsize=(12, 8))

# Create Violin Plot (cut=0 prevents the plot from extending beyond actual data range)
sns.violinplot(
    data=df,
    x='Insurance Type',
    y='Length of Stay (Days)',
    hue='Admission Type',
    palette='Set2',
    inner="quartile", # Draws quartile lines inside the violin
    cut=0  # <--- This parameter prevents the violin plot from extending into negative values!
)

# Add title and axis labels
plt.title('Distribution of Length of Stay by Insurance and Admission Type', fontsize=16)
plt.xlabel('Insurance Type', fontsize=12)
plt.ylabel('Length of Stay (Days)', fontsize=12)

# Set legend title
plt.legend(title='Admission Type')

# Adjust layout and save the plot
plt.tight_layout()
plt.savefig('insurance_los_admission_violinplot.png')
plt.show()