import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. LOAD THE DATASET
# We are using the direct raw URL to the Titanic CSV so it runs immediately for you.
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

print("--- Data Loaded Successfully ---")
print(df.head())

# 2. DATA CLEANING
# Fill missing ages with the average age so our graphs don't break
df['Age'] = df['Age'].fillna(df['Age'].mean())

# 3. ANALYSIS & VISUALIZATION

# Set the visual style
sns.set_theme(style="whitegrid")

# --- Graph 1: Survival Rate by Passenger Class ---
plt.figure(figsize=(8, 6))
sns.barplot(x='Pclass', y='Survived', data=df, errorbar=None, palette="viridis")
plt.title('Survival Rate by Passenger Class')
plt.xlabel('Ticket Class (1 = 1st, 2 = 2nd, 3 = 3rd)')
plt.ylabel('Survival Probability')
plt.savefig('graph1_survival_by_class.png') # Saves the file for your upload
plt.show()

# --- Graph 2: Age Distribution of Passengers ---
plt.figure(figsize=(8, 6))
sns.histplot(df['Age'], bins=20, kde=True, color='skyblue')
plt.title('Distribution of Passenger Ages')
plt.xlabel('Age')
plt.ylabel('Number of Passengers')
plt.savefig('graph2_age_distribution.png') # Saves the file for your upload
plt.show()

# --- Graph 3: Survival Count by Gender ---
plt.figure(figsize=(8, 6))
sns.countplot(x='Sex', hue='Survived', data=df, palette="pastel")
plt.title('Survival Count by Gender')
plt.xlabel('Gender')
plt.ylabel('Number of Passengers')
plt.legend(title='Status', labels=['Died', 'Survived'])
plt.savefig('graph3_survival_by_gender.png') # Saves the file for your upload
plt.show()

# 4. PRINT SUMMARY STATISTICS
print("\n--- Summary Statistics ---")
print(df.groupby('Pclass')['Survived'].mean())
print("\n")
print(df.groupby('Sex')['Survived'].mean())