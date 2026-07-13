import pandas as pd
import os

def clean_hr_data():
    base_dir = r"c:\Users\parag\Music\Data analyst projects\HR Analytics Dashboard"
    source_file = os.path.join(base_dir, "WA_Fn-UseC_-HR-Employee-Attrition.csv")
    dest_file = os.path.join(base_dir, "HR_Data_cleaned.csv")
    
    print("Step 1: Loading raw dataset...")
    df = pd.read_csv(source_file)
    print(f"Original shape: {df.shape}")
    
    print("\nStep 2: Dropping redundant and unnecessary columns...")
    columns_to_drop = [
        'EmployeeCount',      # Always 1
        'Over18',             # Always 'Y'
        'StandardHours',      # Always 80
        'EmployeeNumber',     # Unique ID, not needed for aggregates
        'DailyRate',          # Redundant salary metric
        'HourlyRate',         # Redundant salary metric
        'MonthlyRate'         # Redundant salary metric
    ]
    df = df.drop(columns=columns_to_drop, errors='ignore')
    print(f"Shape after dropping columns: {df.shape}")
    
    print("\nStep 3: Creating conditional column - Age Bracket...")
    def get_age_bracket(age):
        if age >= 51:
            return "51-60"
        elif age >= 41:
            return "41-50"
        elif age >= 31:
            return "31-40"
        elif age >= 21:
            return "21-30"
        else:
            return "18-20"
            
    df['Age Bracket'] = df['Age'].apply(get_age_bracket)
    
    print("Step 4: Creating conditional column - Salary Band (with corrected thresholds)...")
    def get_salary_band(income):
        if income <= 5000:
            return "Low"
        elif income <= 10000:
            return "Medium"
        else:
            return "High"
            
    df['Salary Band'] = df['MonthlyIncome'].apply(get_salary_band)
    
    print(f"Value counts for Salary Band:\n{df['Salary Band'].value_counts()}")
    print(f"Value counts for Age Bracket:\n{df['Age Bracket'].value_counts()}")
    
    print("\nStep 5: Exporting cleaned data to CSV...")
    df.to_csv(dest_file, index=False)
    print(f"Successfully saved cleaned file to: {dest_file}")
    
if __name__ == "__main__":
    clean_hr_data()
