# Social Media Usage Analysis

## Project Overview

This project focuses on analyzing social media engagement across different categories using a simulated dataset. By leveraging Python libraries like **Pandas**, **NumPy**, **Matplotlib**, and **Seaborn**, we explore the distribution of tweet categories, analyze likes, and identify which categories receive the highest engagement.

The project provides insights into user interactions and identifies trends that can help improve content strategy.

---

## Table of Contents

1. [Dataset Description](#dataset-description)  
2. [Libraries Used](#libraries-used)  
3. [Project Steps](#project-steps)  
4. [Visualizations](#visualizations)  
5. [Key Findings](#key-findings)  
6. [Next Steps](#next-steps)  
7. [Code Execution](#code-execution)  

---

## Dataset Description

The dataset contains **500 tweets**, simulated for this analysis, with the following columns:

- **TweetID**: A unique identifier for each tweet.  
- **Category**: The category to which the tweet belongs (e.g., Tech, Health, Sports, Entertainment, Politics).  
- **Likes**: The number of likes each tweet received.  

### Sample Data

| TweetID | Category       | Likes |
|---------|----------------|-------|
| 1       | Tech           | 764   |
| 2       | Health         | 543   |
| 3       | Sports         | 980   |
| 4       | Politics       | 123   |
| 5       | Entertainment  | 456   |

---

## Libraries Used

The following Python libraries were used for data analysis and visualization:

- **Pandas**: For data manipulation and analysis.  
- **NumPy**: For numerical operations.  
- **Matplotlib**: For creating static visualizations.  
- **Seaborn**: For generating advanced, visually appealing plots.

---

## Project Steps

1. **Dataset Creation and Loading**:
   - Simulated a dataset containing 500 records across 5 tweet categories.
   - Loaded the data into a Pandas DataFrame for analysis.

2. **Data Exploration**:
   - Inspected the first few rows using `df.head()`.
   - Generated summary statistics using `df.describe()`.
   - Checked for missing values using `df.isnull().sum()`.

3. **Category Distribution**:
   - Used `value_counts()` to identify the number of tweets in each category.
   - Created a **bar plot** to visualize the category distribution.

4. **Likes Analysis**:
   - **Box Plot**: Analyzed the distribution of likes for each category.
   - **Histogram**: Visualized the overall distribution of likes.
   - **Violin Plot**: Displayed the density of likes across categories.

5. **Mean Likes Calculation**:
   - Grouped the data by category and calculated the mean likes using `groupby()`.

6. **Identifying the Most Popular Category**:
   - Determined which category had the highest average likes.

---

## Visualizations

### 1. Distribution of Categories

![image](https://github.com/user-attachments/assets/fda6bc65-c0d1-4375-b083-d14f73895bc5)


- This bar plot shows the count of tweets in each category.

### 2. Distribution of Likes Across Categories

![image](https://github.com/user-attachments/assets/ad45967f-7132-4b5f-9e4a-33c552fe31e2)


- The box plot displays the spread of likes for each category.

### 3. Overall Distribution of Likes

![image](https://github.com/user-attachments/assets/82993e41-addb-4691-86f6-08b9472390f4)


- This histogram shows how likes are distributed among all tweets.

### 4. Density of Likes Across Categories

![image](https://github.com/user-attachments/assets/77695416-5f17-4353-bf83-2d8670f50d9c)


- The violin plot shows the density and distribution of likes within each category.

---

## Key Findings

1. **Category Distribution**:  
   The tweets are evenly distributed across the following categories: Tech, Health, Sports, Entertainment, and Politics.

2. **Engagement Analysis**:
   - Categories show varying levels of likes.
   - Some categories have higher engagement (likes) than others.

3. **Most Popular Category**:  
   The category with the highest average likes is **identified as follows**:

   ```
   The most popular category is '<Category>' with an average of <Likes> likes.
   ```

4. **Insights**:
   - Engagement is influenced by the category of the tweet.
   - Categories like **Entertainment** and **Tech** tend to perform better in terms of likes.

---

## Next Steps

This project can be extended in the following ways:

1. **Time Analysis**:
   - Analyze how engagement (likes) varies based on the time of posting.

2. **Hashtag Analysis**:
   - Examine which hashtags are associated with higher engagement.

3. **User Demographics**:
   - Incorporate user demographic data (age, location, etc.) to analyze engagement patterns.

4. **Sentiment Analysis**:
   - Use Natural Language Processing (NLP) to understand how sentiment influences likes and engagement.

5. **Comparison with Retweets**:
   - Compare likes and retweets to get a broader picture of user interaction.

---

## Code Execution

To replicate this project, follow these steps:

1. **Dependencies**:
   Install the required libraries using the following command:
   ```bash
   pip install pandas numpy matplotlib seaborn
   ```

2. **Run the Code**:
   Copy the Python script provided in this repository and execute it in your Python environment (e.g., Jupyter Notebook, VSCode, or any IDE).

3. **Visual Outputs**:
   Ensure that Matplotlib and Seaborn plots render correctly in your environment.

---

## Summary

This Social Media Usage Analysis project provides a comprehensive look into how different categories of content perform on social media in terms of likes. By visualizing the data and calculating key metrics, we gain insights into user engagement patterns that can help optimize content strategies for better reach and interaction.

---
