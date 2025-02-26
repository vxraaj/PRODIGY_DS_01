# visualization.py

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Sample data: Age groups and population counts
data = {
    'Age Group': ['0-14', '15-24', '25-54', '55-64', '65+'],
    'Population (millions)': [500, 300, 800, 200, 150]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Create a bar chart
plt.figure(figsize=(10, 6))
sns.barplot(x='Age Group', y='Population (millions)', data=df, palette='viridis')
plt.title('Population Distribution by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Population (millions)')

# Save the plot as an image (optional)
plt.savefig('population_bar_chart.png')

# Show the plot
plt.show()
