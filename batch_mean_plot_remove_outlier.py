import os
import logging
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s:: %(asctime)s - %(message)s')

base_dir = 'data'

def plot_csv_file(folder_name, csv_file_path, png_file_path, mean_record):
    """Plot the data from a CSV file and save the plot."""
    
    # Read the CSV file, skipping the first 3 rows
    df = pd.read_csv(csv_file_path, skiprows=3)
    
    x = df.iloc[:, 0]
    y = df.iloc[:, 1]
    
    # Exclude outliers after frame 600
    frame_600_index = 600
    y_after_600 = y[frame_600_index:]
    mean_without_outliers = np.mean(y_after_600[~is_outlier(y_after_600.values)])
    
    # Record the mean value and action
    action = png_file_path.split(os.path.sep)[1]
    force = png_file_path.split(os.path.sep)[-1].split('.')[0]
    mean_record.append({'Action': f"{action}_{force}", 'Mean Value': mean_without_outliers})
    
    # Plot the data
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, linewidth=1.3)
    plt.xlabel('Time, t (s)', fontsize=14)
    plt.ylabel('Joint Reaction Force, F (N)', fontsize=14)
    #plt.title(f'{action} - {force}')
    
    # Plot mean line
    plt.axhline(y=mean_without_outliers, color='red', linestyle='--', label=f'Mean: {mean_without_outliers:.2f}')
    plt.legend()

    # plt.grid(True)
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
    mean_record = []

    # Loop through 1st Layer subdirectory
    for subdir1 in os.listdir(base_dir):
        subdir1 = os.path.join(base_dir, subdir1)
        
        # Loop through 2nd Layer subdirectory
        for subdir2_folder_name in os.listdir(subdir1):
            csv_dir = os.path.join(subdir1, subdir2_folder_name)
                
            # List only csv files
            if csv_dir.endswith('.csv'):
                save_dir = csv_dir.replace('csv','png')
                plot_csv_file(subdir2_folder_name, csv_dir, save_dir, mean_record)
                logging.info(f"Saving to '{save_dir}' ...... Completed!")
                iter += 1
            else:
                pass

    # Convert mean_record to DataFrame
    mean_df = pd.DataFrame(mean_record)
    
    # Save DataFrame to CSV
    mean_csv_path = 'all_forces_mean_values.csv'
    mean_df.to_csv(mean_csv_path, index=False)

    print('\n=================================================================================================================================')
    logging.info(f'{iter} graphs generated successfully!')
    logging.info(f'Mean values recorded and saved to {mean_csv_path}')
    print('=================================================================================================================================\n')

if __name__ == '__main__':
    main()
