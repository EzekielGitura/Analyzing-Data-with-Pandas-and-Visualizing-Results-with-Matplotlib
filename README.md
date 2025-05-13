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

This happened because recent versions of matplotlib no longer recognize `'seaborn'` as a valid style name. Instead, the correct style names are now `'seaborn-v0_8'`, `'seaborn-darkgrid'`, and similar.

**How I solved it:**  
I updated the line in my code from:
```python
plt.style.use('seaborn')
```

to:
```python
plt.style.use('seaborn-darkgrid')
```
This change allowed the script to run successfully and apply the intended visual style to my plots.

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

## Conclusion

This project provided a hands-on opportunity to work with a well-known dataset and apply essential data analysis and visualization techniques. It reinforced the importance of clear data exploration, thoughtful analysis, and effective communication through visualizations. The Iris dataset remains a valuable resource for learning and practicing these skills.

---