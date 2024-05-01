import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file, skipping the first 3 rows
csv_dir = 'data\S6\S6_CobotDorsiPlantar\Modified_L5SacrumAnteroPosteriorForce.csv'
save_dir = 'data\S6\S6_CobotDorsiPlantar\Modified_L5SacrumAnteroPosteriorForce.png'
df = pd.read_csv(csv_dir, skiprows=3)

x = df.iloc[:, 0]
y = df.iloc[:, 1]

# Plot the data
plt.figure(figsize=(8, 6))
plt.plot(x, y, linewidth=1.1)
plt.xlabel('Time, t (s)', fontsize=12)
plt.ylabel('Joint Reaction Force, F (N)', fontsize=12)

if 'AnteroPosterior' in csv_dir:
    plt.title('L5 Sacrum Antero Posterior Force')
elif 'MedioLateral' in csv_dir:
    plt.title('L5 Sacrum Medio Lateral Force')
else:
    plt.title('L5 Sacrum Proximo Distal Force')

#plt.grid(True)
plt.savefig(save_dir)
plt.show()
