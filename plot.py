import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file, skipping the first 3 rows
csv_dir = 'data/L5SacrumProximoDistalForce.csv'
df = pd.read_csv(csv_dir, skiprows=3)

x = df.iloc[:, 0]
y = df.iloc[:, 1]

# Plot the data
plt.plot(x, y)
plt.xlabel('Time, t (s)')
plt.ylabel('Joint Reaction Force, F (N)')

if 'AnteroPosterior' in csv_dir:
    plt.title('L5 Sacrum Antero Posterior Force')
elif 'MedioLateral' in csv_dir:
    plt.title('L5 Sacrum Medio Lateral Force')
else:
    plt.title('L5 Sacrum Proximo Distal Force')

plt.grid(True)
plt.show()
