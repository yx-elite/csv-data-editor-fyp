import os
import logging
import pandas as pd
import matplotlib.pyplot as plt


# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s:: %(asctime)s - %(message)s')

base_dir = 'S5_data'

def plot_csv_file(csv_file_path, png_file_path):
    """Plot the data from a CSV file and save the plot."""
    
    # Read the CSV file, skipping the first 3 rows
    df = pd.read_csv(csv_file_path, skiprows=3)

    x = df.iloc[:, 0]   # Time column
    y = df.iloc[:, 5]   # REBA column

    # Plot the data
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, linewidth=1.3)
    plt.xlabel('Time, t (s)', fontsize=12)
    plt.ylabel('Joint Reaction Force, F (N)', fontsize=12)

    # plt.grid(True)
    plt.savefig(png_file_path)
    plt.close()

def main():
    """Main program to loop files through all subdirectories."""
    
    iter = 0
    # Loop through S5_data folder
    for subdir1 in os.listdir(base_dir):
        subdir1 = os.path.join(base_dir, subdir1)
        
        # Loop through every files in the subdirectory
        for file_path in os.listdir(subdir1):
            # List only csv files
            if file_path.endswith('.csv'):
                csv_dir = os.path.join(subdir1, file_path)
                
                if 'reba' in csv_dir.lower():
                    save_dir = csv_dir.replace('csv','png')
                    plot_csv_file(csv_dir, save_dir)
                    iter += 1
                    #logging.info(f"Saving to '{save_dir}' ...... Completed!")
    
    print('\n=================================================================================================================================')
    logging.info(f'{iter} graphs generated successfully!')
    print('=================================================================================================================================\n')


if __name__ == '__main__':
    main()