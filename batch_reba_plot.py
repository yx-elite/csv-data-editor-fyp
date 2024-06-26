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
    df = pd.read_csv(csv_file_path, skiprows=1)

    x = df.iloc[:, 0]   # Time column
    y = df.iloc[:, 5]   # REBA column

    # Plot the data
    plt.figure(figsize=(8, 6))
    plt.rcParams.update({'font.size': 12})
    plt.plot(x, y, linewidth=1.3, color='black')
    #plt.xlim(left=0)
    plt.ylim([0, 15])
    plt.xlabel('Time, t (s)', fontsize=16)
    plt.ylabel('REBA Score', fontsize=16)
    
    #plt.grid(True)
    plt.axhspan(10, 15, facecolor='#e9b3b3')
    plt.axhspan(7, 10, facecolor='#f5e4c8')
    plt.axhspan(3, 7, facecolor='#f4f1c9')
    plt.axhspan(1, 3, facecolor='#d8ecd6')
    plt.axhspan(0, 1, facecolor='#c8cff5')
    
    plt.savefig(png_file_path)
    plt.close()

def main():
    """Main program to loop files through all subdirectories."""
    
    iter = 0
    # Loop through S5_data folder
    for subfolder in os.listdir(base_dir):
        subdir = os.path.join(base_dir, subfolder)
        
        # Loop through every files in the subdirectory
        for file_path in os.listdir(subdir):
            # List only csv files
            if file_path.endswith('.csv'):
                csv_dir = os.path.join(subdir, file_path)
                # Check reba.csv in each directory
                if 'reba' in csv_dir.lower():
                    reba_img = f'{subfolder}.png'
                    save_dir = os.path.join('reba_score', reba_img)
                    plot_csv_file(csv_dir, save_dir)
                    iter += 1
                    logging.info(f"Saving to '{save_dir}' ...... Completed!")
    
    print('\n=================================================================================================================================')
    logging.info(f'{iter} graphs generated successfully!')
    print('=================================================================================================================================\n')


if __name__ == '__main__':
    main()