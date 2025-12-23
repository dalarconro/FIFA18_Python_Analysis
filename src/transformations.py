import pandas as pd
import numpy as np
import re

###############################
# STEP 1. FILTERING THE DATASET
###############################

# Function to filter columns of the DataFrame
def filter(data: pd.DataFrame) -> pd.DataFrame:
    """
    Filtering DataFrame columns
    """
    # Selecting only the columns that we are gonna use
    filtered_cols = data.loc[:, ['Name', 'Age', 'Nationality', 'Overall', 'Potential', 'International Reputation', 'Club', 'Wage', 
                            'Preferred Foot', 'Weak Foot', 'Position', 'Jersey Number', 'Height', 'Weight', 'Joined', 
                            'Contract Valid Until', 'Release Clause']]

    return filtered_cols



###################################
# STEP 2. TRANSFORMING THE DATASET
###################################

def convert_height_to_cm(height_str):
    """
    Convert 5'11 format to centimeters (float)
    """
    if pd.isna(height_str) or "'" not in str(height_str):
        return np.nan
    
    try:
        feet_str, inches_str = height_str.split("'")
        feet = int(feet_str)
        inches = int(inches_str)
        
        # (Foot * 12 + inches) * 2.54
        total_inches = (feet * 12) + inches
        return round(total_inches * 2.54, 2)
    except:
        return np.nan


def convert_weight_to_kg(weight_str):
    """
    Convert '165lbs' format to kilograms (float)
    """
    if pd.isna(weight_str):
        return np.nan
    
    try:
        # Remove 'lbs' and convert to float
        lbs = float(str(weight_str).replace('lbs', ''))
        return round(lbs * 0.453592, 2)
    except:
        return np.nan


def convert_currency_to_float(value):
    """
    Convert currency strings (ex: '€100K', '€10.5M') to float values.
    Deals with messing values returning 0.0.
    """
    if pd.isna(value) or value == '0' or value == '':
        return 0.0
    
    # Convert to string to be safe
    value = str(value).strip()
    
    # REGEX: Keep only numbers, dots, and the letters K or M
    # This ignores the Euro symbol regardless of its encoding
    value = re.sub(r'[^\d.KMkm]', '', value)
    
    if not value:
        return 0.0

    if 'M' in value.upper():
        return float(value.upper().replace('M', '')) * 1_000_000
    elif 'K' in value.upper():
        return float(value.upper().replace('K', '')) * 1_000
    
    try:
        return float(value)
    except ValueError:
        return 0.0


def clean_dates(df):
    """
    Standarize date columns.
    """
    df = df.copy()

    # 1. Clean 'Joined'
    # errors='coerce' will transform extrange or missing values to NaT (Not a Time)
    df['Joined'] = pd.to_datetime(df['Joined'], errors='coerce')

    # 2. Clean 'Contract Valid Until'
    def parse_contract_date(value):
        if pd.isna(value):
            return pd.NaT
        
        value = str(value).strip()
        
        # If value is only the year (ex: '2021'), we add day and month
        if len(value) == 4 and value.isdigit():
            return pd.to_datetime(f"Dec 31, {value}")
        
        # If it is a complete date or any other format
        return pd.to_datetime(value, errors='coerce')

    df['Contract Valid Until'] = df['Contract Valid Until'].apply(parse_contract_date)
    
    return df


def group_positions(df):
    """
    Groups the 27 specific FIFA positions into 4 main categories:
    GK, DEF, MDF, ATT.
    """
    df = df.copy()
    
    # Mapping dictionary based on tactical roles
    nested_positions = {
        'GK': ['GK'], # Goalkeepers
        # Defenders (Center Backs, Full Backs, and Wing Backs)
        'DEF': ['CB', 'RCB', 'LCB', 'LB', 'RB', 'LWB', 'RWB'],
        # Midfielders (Defensive, Central, Attacking, and Wide Midfielders)
        'MDF': ['CM', 'LCM', 'RCM', 'CDM', 'LDM', 'RDM', 'CAM', 'LAM', 'RAM', 'LM', 'RM'],
        # Attackers (Strikers, Center Forwards, and Wingers)
        'ATT': ['ST', 'LS', 'RS', 'CF', 'RF', 'LF', 'LW', 'RW']
    }

    # Transform it into a flat dictionary (Fast for Python)
    pos_map = {v: k for k, values in nested_positions.items() for v in values}

    # Now pos_map is: {'GK': 'GK', 'CB': 'DEF', 'RCB': 'DEF', ...}
    # Create a new column 'Position_Group' to store the categories
    # map() will apply the dictionary logic to every row in the 'Position' column
    df['Position_Group'] = df['Position'].map(pos_map)
    
    # Fill any unmapped positions with 'Other'
    df['Position_Group'] = df['Position_Group'].fillna('Other')

    # 3. Reorder columns
    cols = list(df.columns)
    # Find the index of 'Position' and insert 'Position_Group' right after it
    # We remove it from the end first (where it was added by default)
    cols.remove('Position_Group')
    pos_idx = cols.index('Position')
    cols.insert(pos_idx + 1, 'Position_Group')
    
    return df[cols]


def data_adjustment(data: pd.DataFrame) -> pd.DataFrame:
    """
    Calling transformation functions to adjust the DataFrame to the desired format
    """
    df = data.copy()

    # Converting Height and Weight to IS units
    # Check Weight: only transform if it's still an 'object' (string)
    if df['Weight'].dtype == 'object':
        df['Weight'] = df['Weight'].apply(convert_weight_to_kg)
        
    # Check Height: same logic
    if df['Height'].dtype == 'object':
        df['Height'] = df['Height'].apply(convert_height_to_cm)

    # Apply convertion to currency columns
    currency_cols = ['Wage', 'Release Clause']
    for col in currency_cols:
        # Check currency cols: only transform if it's still an 'object' (string)
        if df[col].dtype == 'object':
            df[col] = df[col].apply(convert_currency_to_float)
    
    # Cleaning date columns
    df = clean_dates(df)

    # Mapping positions
    df = group_positions(df)
        
    return df



######################################
# STEP 3. DEALING WITH MISSING VALUES
######################################

def missing_treatment(data: pd.DataFrame) -> pd.DataFrame:
    """
    Filling or dropping missing values using reassignment.
    """
    df = data.copy()

    # 1. Drop rows with missing values in critical columns
    df = df.dropna(subset=['Name', 'Overall', 'Potential', 'Position'])

    # Strings: Categorical replacements
    df['Nationality'] = df['Nationality'].fillna('Unknown')
    df['Club'] = df['Club'].fillna('Free Agent')
    df['Preferred Foot'] = df['Preferred Foot'].fillna('Right')
    
    # Financials & Numbers
    df['Wage'] = df['Wage'].fillna(0)
    df['Release Clause'] = df['Release Clause'].fillna(0)
    df['Jersey Number'] = df['Jersey Number'].fillna(0)
    
    # Weak Foot and International Reputation: Replace with minimum
    df['Weak Foot'] = df['Weak Foot'].fillna(df['Weak Foot'].min())
    df['International Reputation'] = df['International Reputation'].fillna(df['International Reputation'].min())
    
    # Age, Height and Weight: Replace with mean
    df['Age'] = df['Age'].fillna(round(df['Age'].mean(), 2))
    df['Height'] = df['Height'].fillna(round(df['Height'].mean(), 2))
    df['Weight'] = df['Weight'].fillna(round(df['Weight'].mean(), 2))
    
    # Contract: Standardize nulls to a specific date
    df['Joined'] = df['Joined'].fillna(pd.to_datetime('Jan 31, 2019'))
    df['Contract Valid Until'] = df['Contract Valid Until'].fillna(pd.to_datetime('Dec 31, 2018'))

    return df



##############################
# STEP 4. CASTING TO INTEGERS
##############################

def cast_to_integer(data: pd.DataFrame) -> pd.DataFrame:
    """
    Cast float columns to integer.
    """
    df = data.copy()
    
    int_columns = ['International Reputation', 'Weak Foot', 'Jersey Number']
    
    for col in int_columns:
        # 1. Limpieza básica: rellenar nulos con 0 para poder convertir a int
        # Si prefieres mantener los nulos, usaríamos .astype('Int64')
        df[col] = df[col].astype(int)
        
    return df



####################################
# STEP 5. UNIT SCALING AND RENAMING
####################################

def scale_rename(data: pd.DataFrame) -> pd.DataFrame:
    """
    Renaming and scaling columns to include the unit associated to its value.
    """

    # 1. Scaling to desired units (Wage to K, Release Clause to M)
    # We do this here to keep the transformations.py logic simple and standard
    if 'Wage' in data.columns:
        data['Wage'] = data['Wage'] / 1_000
    if 'Release Clause' in data.columns:
        data['Release Clause'] = data['Release Clause'] / 1_000_000

    # 2. Renaming for clarity in Analysis
    rename_dict = {
        'Wage': 'Wage (K_EUR)',
        'Release Clause': 'Release Clause (M_EUR)',
        'Height': 'Height_cm',
        'Weight': 'Weight_kg'
    }

    data_final = data.rename(columns=rename_dict)

    return data_final