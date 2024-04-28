import random
import logging
import pandas as pd

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s:: %(asctime)s - %(message)s')

# subject_ref = input('Enter the subject reference (For eg. S1)\t: ')
# trial_ref = input('Enter the trial reference (For eg. 01)\t\t: ')

print('\n\t[0] - Posterior   [1] - Lateral   [2] - Distal\n')
L5_selection = input('Choose the L5 force accordingly (For eg. 0)\t: ')

# Load and set the dataframe range to be modified
match L5_selection:
    case '0':
        original_df = pd.read_csv('data/L5SacrumAnteroPosteriorForce.csv', header=None, nrows=3)
        modified_df = pd.read_csv('data/L5SacrumAnteroPosteriorForce.csv', header=None, skiprows=3)
    case '1':
        original_df = pd.read_csv('data/L5SacrumMedioLateralForce.csv', header=None, nrows=3)
        modified_df = pd.read_csv('data/L5SacrumMedioLateralForce.csv', header=None, skiprows=3)
    case '2':
        original_df = pd.read_csv('data/L5SacrumProximoDistalForce.csv', header=None, nrows=3)
        modified_df = pd.read_csv('data/L5SacrumProximoDistalForce.csv', header=None, skiprows=3)

# Modify the cloned dataframe
for i in range(2, len(modified_df)):
    match L5_selection:
        case '0':
            rand_int = random.randint(-100, 100)
        case '1':
            rand_int = random.randint(-20, 20)
        case '2':
            rand_int = random.randint(-200, 200)
    
    modified_df.iloc[i, 1] += rand_int
    print(f'Modifying Row [{i}]............ {modified_df.iloc[i, 1]:.10f} ({rand_int})')

logging.info('All values are modified successfully')

# Save the modified DataFrame to a new CSV file
modified_df = pd.concat([original_df, modified_df])
match L5_selection:
    case '0':
        modified_df.to_csv('modified_data/Modified_L5SacrumAnteroPosteriorForce.csv', index=False, header=False)
    case '1':
        modified_df.to_csv('modified_data/Modified_L5SacrumMedioLateralForce.csv', index=False, header=False)
    case '2':
        modified_df.to_csv('modified_data/Modified_L5SacrumProximoDistalForce.csv', index=False, header=False)

logging.info('Modified dataFrame saved to CSV successfully')