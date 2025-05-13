import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Error handling for data loading
try:
    # Load the Iris dataset
    iris = load_iris()
    df = pd.DataFrame(data=np.c_[iris['data'], iris['target']], 
                     columns=iris['feature_names'] + ['target'])
    
    # Convert target numbers to species names
    species_names = {0: 'setosa', 1: 'versicolor', 2: 'virginica'}
    df['species'] = df['target'].map(species_names)
    
    # Task 1: Data Exploration
    print("First few rows of the dataset:")
    print(df.head())
    
    print("\nDataset Info:")
    print(df.info())
    
    print("\nChecking for missing values:")
    print(df.isnull().sum())
    
    # Task 2: Basic Data Analysis
    print("\nBasic statistics of numerical columns:")
    print(df.describe())
    
    print("\nMean values by species:")
    print(df.groupby('species')[iris['feature_names']].mean())
    
    # Task 3: Data Visualization
    sns.set(style="darkgrid")
    
    # Create a figure with subplots
    fig = plt.figure(figsize=(15, 10))
    
    # 1. Line plot
    plt.subplot(2, 2, 1)
    for species in species_names.values():
        species_data = df[df['species'] == species]
        plt.plot(species_data['sepal length (cm)'].values, label=species)
    plt.title('Sepal Length Patterns')
    plt.xlabel('Sample Index')
    plt.ylabel('Sepal Length (cm)')
    plt.legend()
    
    # 2. Bar plot
    plt.subplot(2, 2, 2)
    df.groupby('species')['petal length (cm)'].mean().plot(kind='bar')
    plt.title('Average Petal Length by Species')
    plt.xlabel('Species')
    plt.ylabel('Average Petal Length (cm)')
    
    # 3. Histogram
    plt.subplot(2, 2, 3)
    for species in species_names.values():
        species_data = df[df['species'] == species]
        plt.hist(species_data['sepal width (cm)'], alpha=0.5, label=species)
    plt.title('Distribution of Sepal Width')
    plt.xlabel('Sepal Width (cm)')
    plt.ylabel('Frequency')
    plt.legend()
    
    # 4. Scatter plot
    plt.subplot(2, 2, 4)
    for species in species_names.values():
        species_data = df[df['species'] == species]
        plt.scatter(species_data['sepal length (cm)'], 
                   species_data['petal length (cm)'], 
                   label=species, alpha=0.5)
    plt.title('Sepal Length vs Petal Length')
    plt.xlabel('Sepal Length (cm)')
    plt.ylabel('Petal Length (cm)')
    plt.legend()
    
    plt.tight_layout()
    plt.show()

except Exception as e:
    print(f"An error occurred: {str(e)}")
