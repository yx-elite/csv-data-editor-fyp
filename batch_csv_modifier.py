import os
import logging
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s:: %(asctime)s - %(message)s')

base_dir = 'data'

def plot_and_modify_csv_file(folder_name, csv_file_path, png_file_path):
    """Plot the data from a CSV file, modify y-values, and save the plot."""
    
    # Read the CSV file, skipping the first 3 rows
    df = pd.read_csv(csv_file_path, skiprows=3)
    
    x = df.iloc[:, 0]
    y = df.iloc[:, 1]
    
    # Exclude outliers after frame 600
    frame_600_index = 400
    y_after_600 = y[frame_600_index:]
    non_outlier_indices = ~is_outlier(y_after_600.values)
    y.loc[frame_600_index + np.where(non_outlier_indices)[0]] -= 1000
    
    # Save the modified DataFrame back to the original CSV
    df_modified = pd.concat([x, y], axis=1)
    df_modified.columns = df.columns
    df_modified.to_csv(csv_file_path, index=False)
    
    # Plot the original and modified data
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, linewidth=1.3, label='Modified Data')
    plt.xlabel('Time, t (s)', fontsize=12)
    plt.ylabel('Joint Reaction Force, F (N)', fontsize=12)
    plt.savefig(png_file_path)
    plt.close()

def is_outlier(points, threshold=3.5):
    """Identify outliers based on modified Z-score method."""
    if len(points.shape) == 1:
        points = points[:, None]
    median = np.median(points, axis=0)
    diff = np.sum((points - median)**2, axis=-1)
    diff = np.sqrt(diff)
    med_abs_deviation = np.median(diff)

    modified_z_score = 0.6745 * diff / med_abs_deviation

    return modified_z_score > threshold

def main():
    """Main program to loop files through all subdirectories."""
    
    iter = 0

    # Loop through 1st Layer subdirectory
    for subdir1 in os.listdir(base_dir):
        subdir1_path = os.path.join(base_dir, subdir1)
        
        if 'cobot' in subdir1_path.lower():
            # Loop through 2nd Layer subdirectory
            for subdir2_folder_name in os.listdir(subdir1_path):
                csv_dir = os.path.join(subdir1_path, subdir2_folder_name)
                    
                # List only csv files
                if csv_dir.endswith('.csv') and 'proximo' in csv_dir.lower():
                    save_dir = csv_dir.replace('csv','png')
                    plot_and_modify_csv_file(subdir2_folder_name, csv_dir, save_dir)
                    logging.info(f"Modifying '{csv_dir}' ...... Completed!")
                    iter += 1
                else:
                    pass
        else:
            logging.info(f"'Cobot' not found! Skipping ... '{subdir1_path}'")

    print('\n=================================================================================================================================')
    logging.info(f'{iter} graphs generated and CSV files modified successfully!')
    print('=================================================================================================================================\n')

if __name__ == '__main__':
    main()
