import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
# For the purpose of this project, we'll simulate a dataset
np.random.seed(42)

categories = ['Tech', 'Health', 'Sports', 'Entertainment', 'Politics']
data = {
    'TweetID': range(1, 501),
    'Category': np.random.choice(categories, 500),
    'Likes': np.random.randint(0, 1000, 500)
}

df = pd.DataFrame(data)

# Display the first few rows of the dataset
df.head()

# Summary statistics
df.describe()

# Check for missing values
df.isnull().sum()

# Distribution of categories
category_counts = df['Category'].value_counts()
print(category_counts)

# Set the style for seaborn
sns.set(style="whitegrid")

# Bar plot for the distribution of categories
plt.figure(figsize=(10, 6))
sns.countplot(x='Category', data=df, palette='viridis')
plt.title('Distribution of Categories')
plt.xlabel('Category')
plt.ylabel('Count')
plt.show()

# Box plot to show the distribution of likes in different categories
plt.figure(figsize=(10, 6))
sns.boxplot(x='Category', y='Likes', data=df, palette='viridis')
plt.title('Distribution of Likes Across Categories')
plt.xlabel('Category')
plt.ylabel('Likes')
plt.show()

# Histogram of likes
plt.figure(figsize=(10, 6))
sns.histplot(df['Likes'], bins=30, kde=True, color='blue')
plt.title('Distribution of Likes')
plt.xlabel('Likes')
plt.ylabel('Frequency')
plt.show()

# Violin plot to show the density of likes across categories
plt.figure(figsize=(10, 6))
sns.violinplot(x='Category', y='Likes', data=df, palette='viridis')
plt.title('Density of Likes Across Categories')
plt.xlabel('Category')
plt.ylabel('Likes')
plt.show()


# Violin plot to show the density of likes across categories
plt.figure(figsize=(10, 6))
sns.violinplot(x='Category', y='Likes', data=df, palette='viridis')
plt.title('Density of Likes Across Categories')
plt.xlabel('Category')
plt.ylabel('Likes')
plt.show()

# Calculate the mean likes for each category
mean_likes = df.groupby('Category')['Likes'].mean().reset_index()
print(mean_likes)

# Identify the category with the highest mean likes
most_popular_category = mean_likes.loc[mean_likes['Likes'].idxmax()]
print(f"The most popular category is {most_popular_category['Category']} with an average of {most_popular_category['Likes']} likes.")

# Summary of findings
print("Summary of Findings:")
print(f"1. The dataset contains {len(df)} tweets distributed across {len(categories)} categories.")
print("2. The distribution of likes shows that certain categories receive more engagement than others.")
print(f"3. The category '{most_popular_category['Category']}' has the highest average likes, indicating higher user engagement.")
print("4. Further analysis could include examining the impact of time of day, hashtags, and user demographics on engagement.")
