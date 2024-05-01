import os
import random
import logging
import pandas as pd

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s:: %(asctime)s - %(message)s')

# Define original path for raw data
base_dir = 'data/S4'
trial_folder = 'S4_CobotDorsiPlantar'
trial_dir = os.path.join(base_dir, trial_folder)

# Define save path for modified data
base_save_dir = 'data'
save_path = 'S6'
save_dir = os.path.join(base_save_dir, save_path)


print('\n\t[0] - Posterior   [1] - Lateral   [2] - Distal\n')
L5_selection = input('Choose the L5 force accordingly (For eg. 0)\t: ')

# Load and set the dataframe range to be modified
match L5_selection:
    case '0':
        original_df = pd.read_csv(os.path.join(trial_dir, 'L5SacrumAnteroPosteriorForce.csv'), header=None, nrows=3)
        modified_df = pd.read_csv(os.path.join(trial_dir, 'L5SacrumAnteroPosteriorForce.csv'), header=None, skiprows=3)
    case '1':
        original_df = pd.read_csv(os.path.join(trial_dir, 'L5SacrumMedioLateralForce.csv'), header=None, nrows=3)
        modified_df = pd.read_csv(os.path.join(trial_dir, 'L5SacrumMedioLateralForce.csv'), header=None, skiprows=3)
    case '2':
        original_df = pd.read_csv(os.path.join(trial_dir, 'L5SacrumProximoDistalForce.csv'), header=None, nrows=3)
        modified_df = pd.read_csv(os.path.join(trial_dir, 'L5SacrumProximoDistalForce.csv'), header=None, skiprows=3)

# Modify the cloned dataframe
for i in range(2, len(modified_df)):
    match L5_selection:
        case '0':
            rand_int = random.randint(0, 20)
        case '1':
            rand_int = random.randint(-20, 20)
        case '2':
            rand_int = random.randint(-200, 200)
    
    modified_df.iloc[i, 1] += rand_int
    print(f'Modifying Row [{i}]............ {modified_df.iloc[i, 1]:.10f} ({rand_int})')

logging.info('All values are modified successfully')

# Save the modified DataFrame to a new CSV file
modified_df = pd.concat([original_df, modified_df])
full_save_dir = os.path.join(save_dir, f'{save_path}_{trial_folder[3:]}')

while True:
    try:
        match L5_selection:
            case '0':
                modified_df.to_csv(os.path.join(full_save_dir, 'Modified_L5SacrumAnteroPosteriorForce.csv'), index=False, header=False)
                break
            case '1':
                modified_df.to_csv(os.path.join(full_save_dir, 'Modified_L5SacrumMedioLateralForce.csv'), index=False, header=False)
                break
            case '2':
                modified_df.to_csv(os.path.join(full_save_dir, 'Modified_L5SacrumProximoDistalForce.csv'), index=False, header=False)
                break
    
    except Exception as e:
        os.makedirs(full_save_dir)

logging.info('Modified dataFrame saved to CSV successfully.')