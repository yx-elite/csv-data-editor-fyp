import os
import logging
import pandas as pd
import matplotlib.pyplot as plt


# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s:: %(asctime)s - %(message)s')

base_dir = 'data'

def plot_csv_file(folder_name, csv_file_path, png_file_path):
    """Plot the data from a CSV file and save the plot."""
    
    # Read the CSV file, skipping the first 3 rows
    df = pd.read_csv(csv_file_path, skiprows=3)

    x = df.iloc[:, 0]
    y = df.iloc[:, 1]

    # Plot the data
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, linewidth=1.3)
    plt.xlabel('Time, t (s)', fontsize=12)
    plt.ylabel('Joint Reaction Force, F (N)', fontsize=12)

    if 'AnteroPosterior' in csv_file_path:
        plt.title(f'{folder_name} - L5 Sacrum Antero Posterior Force')
    elif 'MedioLateral' in csv_file_path:
        plt.title(f'{folder_name} - L5 Sacrum Medio Lateral Force')
    else:
        plt.title(f'{folder_name} - L5 Sacrum Proximo Distal Force')

    # plt.grid(True)
    plt.savefig(png_file_path)
    plt.close()

def main():
    """Main program to loop files through all subdirectories."""
    iter = 0
    # Loop through 1st Layer subdirectory
    for subdir1 in os.listdir(base_dir):
        subdir1 = os.path.join(base_dir, subdir1)
        
        # Loop through 2nd Layer subdirectory
        for subdir2_folder_name in os.listdir(subdir1):
            subdir2 = os.path.join(subdir1, subdir2_folder_name)
            
            # Loop through every files in the subdirectory
            for file_path in os.listdir(subdir2):
                # List only csv files
                if file_path.endswith('.csv'):
                    
                    # Initialise the 
                    csv_dir = os.path.join(subdir2, file_path)
                    save_dir = csv_dir.replace('csv','png')
                    plot_csv_file(subdir2_folder_name, csv_dir, save_dir)
                    iter += 1
                    logging.info(f"Saving to '{save_dir}' ...... Completed!")
    
    print('\n=================================================================================================================================')
    logging.info(f'{iter} graphs generated successfully!')
    print('=================================================================================================================================\n')


if __name__ == '__main__':
    main()