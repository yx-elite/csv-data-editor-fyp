import os
import logging
import pandas as pd
import matplotlib.pyplot as plt

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s:: %(asctime)s - %(message)s')

base_dir = 'data'
rehab = 'Cpst'
trials = ['DorsiPlantar', 
         'HipAbdadd', 
         'HipFlex', 
         'KneeFlexExtens',
         'KneeRot']

def plot_csv_file(folder_name, itvn_csv_path, cvtn_csv_path, png_file_path):
    """Plot the data from two CSV files on the same graph and save the plot."""
    
    # Read the CSV files, skipping the first 3 rows
    itvn_df = pd.read_csv(itvn_csv_path, skiprows=3)
    cvtn_df = pd.read_csv(cvtn_csv_path, skiprows=3)
    
    itvn_x = itvn_df.iloc[:, 0]
    itvn_y = itvn_df.iloc[:, 1]
    
    cvtn_x = cvtn_df.iloc[:, 0]
    cvtn_y = cvtn_df.iloc[:, 1]
    
    # Plot the data
    plt.figure(figsize=(8, 6))
    
    if 'Cobot' in rehab:
        plt.plot(itvn_x, itvn_y, label='Collaborative Robot', linewidth=1.3)
    else:
        plt.plot(itvn_x, itvn_y, label='Weight Compensator', linewidth=1.3)
    
    plt.plot(cvtn_x, cvtn_y, label='Conventional', linewidth=1.3)
    plt.xlabel('Time, t (s)', fontsize=12)
    plt.ylabel('Joint Reaction Force, F (N)', fontsize=12)
    plt.title(f'{folder_name} - Joint Reaction Force against Time')
    plt.legend()
    #plt.grid(True)
    plt.savefig(png_file_path)
    plt.close()

def main():
    """Main program to loop files through all subdirectories."""
    
    itvn_dorsi = []
    cvtn_dorsi = []
    
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
                    
                    # Initialize the paths
                    csv_dir = os.path.join(subdir2, file_path)
                    
                    for trial in trials:
                        if rehab.lower() in csv_dir.lower() and trial.lower() in csv_dir.lower():
                            itvn_dorsi.append(csv_dir)
                        
                        if 'cvtn' in csv_dir.lower() and trial.lower() in csv_dir.lower():
                            cvtn_dorsi.append(csv_dir)
    
    iter = 0
    # Pair up itvn and cvtn for comparison and plot
    for itvn_file, cvtn_file in zip(itvn_dorsi, cvtn_dorsi):
        folder_name = os.path.basename(os.path.dirname(itvn_file))
        png_file_path = os.path.join('comparison_data', f"{itvn_file.split(os.path.sep)[2]}_{itvn_file.split(os.path.sep)[-1].split('.')[0]}.png")
        plot_csv_file(folder_name, itvn_file, cvtn_file, png_file_path)
        iter += 1
        logging.info(f"Saving to '{png_file_path}' ...... Completed!")
    
    print('\n=================================================================================================================================')
    logging.info(f'{iter} graphs generated successfully!')
    print('=================================================================================================================================\n')



if __name__ == '__main__':
    main()