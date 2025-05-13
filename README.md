# Analyzing Data with Pandas and Visualizing Results with Matplotlib

## Project Overview

In this project, I explored the classic **Iris dataset** to practice and demonstrate data analysis and visualization skills using Python. The main objectives were to load, clean, analyze, and visualize the dataset, while applying best practices in error handling and code organization.

---

## Project Objectives

- Load and explore a real-world dataset (the Iris dataset, accessed via the UCI Machine Learning Repository).
- Analyze the data using **pandas**.
- Visualize the results with **matplotlib** and **seaborn**.
- Ensure the process is robust with proper error handling.

---

## Methodology

### 1. Getting the Data
I used the `sklearn.datasets.load_iris()` function to access the Iris dataset directly in Python. This dataset contains measurements for 150 iris flowers, covering three species: *setosa*, *versicolor*, and *virginica*.

### 2. Exploring the Data
- **Initial Inspection:** Displayed the first few rows with `.head()` to get an overview.
- **Structure Check:** Used `.info()` to review data types and `.isnull().sum()` to check for missing values.
- **Cleaning:** Although the Iris dataset is already clean, I included steps to handle missing values if they were present.

### 3. Basic Data Analysis
- **Descriptive Statistics:** Used `.describe()` to summarize the numerical columns.
- **Grouping:** Grouped the data by species to compare measurements across the three types.

### 4. Data Visualization
I created four types of plots to better understand and communicate the data:
- **Line Chart:** Showed trends in sepal length for each species.
- **Bar Chart:** Compared average petal lengths across species.
- **Histogram:** Illustrated the distribution of sepal widths.
- **Scatter Plot:** Explored the relationship between sepal length and petal length.

All plots were customized with clear titles, axis labels, and legends. I used **matplotlib** for plotting and **seaborn** for enhanced visual style.

### 5. Error Handling
The code is wrapped in a `try-except` block to gracefully handle potential issues such as missing files or data type mismatches.

---

## Tools Used

- **Python**: Main programming language.
- **pandas**: For data manipulation and analysis.
- **numpy**: For numerical operations.
- **matplotlib**: For creating visualizations.
- **seaborn**: For improved plot aesthetics.
- **scikit-learn**: For loading the Iris dataset.
- **Jupyter Notebook / VS Code**: For developing and running the code.

---

## What I Learned

- How to load and inspect real-world datasets.
- Effective use of pandas for data analysis.
- Grouping and summarizing data to extract insights.
- Creating and customizing visualizations to communicate findings.
- The importance of robust error handling in data projects.

---

## Challenges Faced

During the visualization step, I encountered the following error:

```
An error occurred: 'seaborn' is not a valid package style, path of style file, URL of style file, or library style name (library styles are listed in `style.available`)
```

Initially, I tried to set the plot style using `plt.style.use('seaborn')` and other similar style names, but none of these worked with my matplotlib version.

**How I solved it:**  
Instead of using `plt.style.use`, I set the style directly with seaborn using:
```python
sns.set(style="darkgrid")
```
This approach worked perfectly and applied the intended visual style to my plots.

---

## How to Run This Project

1. **Clone this repository** or download the files.
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the script**:
   ```bash
   python data_analysis.py
   ```
   Alternatively, open the notebook in Jupyter for an interactive experience.

---

## Sample Output

When you run the script, you will see:
- Console output showing the first few rows of the dataset, data info, missing value check, descriptive statistics, and mean values by species.
- A window with four plots:
    - **Line Chart:** Sepal length patterns for each species.
    - **Bar Chart:** Average petal length by species.
    - **Histogram:** Distribution of sepal width for each species.
    - **Scatter Plot:** Sepal length vs. petal length, colored by species.

Example console output:
```
First few rows of the dataset:
   sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)  target  species
0                5.1               3.5                1.4               0.2     0.0   setosa
1                4.9               3.0                1.4               0.2     0.0   setosa
2                4.7               3.2                1.3               0.2     0.0   setosa
3                4.6               3.1                1.5               0.2     0.0   setosa
4                5.0               3.6                1.4               0.2     0.0   setosa

Dataset Info:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 150 entries, 0 to 149
...
```
And a figure with four well-labeled plots for visual analysis.

---

## Conclusion

This project provided a hands-on opportunity to work with a well-known dataset and apply essential data analysis and visualization techniques. It reinforced the importance of clear data exploration, thoughtful analysis, and effective communication through visualizations. The Iris dataset remains a valuable resource for learning and practicing these skills.

---