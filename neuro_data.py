# neuro_analysis.py
import pandas as pd
import matplotlib.pyplot as plt

def load_data():
    url = "https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv"
    df = pd.read_csv(url)
    print("Data loaded successfully.")
    return df

def describe_data(df):
    print("\n--- Dataset Summary ---")
    print(df.describe())
    print("\n--- Null Values ---")
    print(df.isnull().sum())

def plot_data(df):
    plt.figure()
    df.plot(kind='scatter', x='Height(Inches)', y='Weight(Pounds)', alpha=0.5)
    plt.title('Height vs. Weight (sample neuro proxy)')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('height_vs_weight.png')
    print("Plot saved as height_vs_weight.png")

def clean_data(df):
    # Remove rows with any missing values
    df = df.dropna()

    # Remove outliers: unrealistic height or weight values
    df = df[(df['Height(Inches)'] > 50) & (df['Height(Inches)'] < 85)]
    df = df[(df['Weight(Pounds)'] > 80) & (df['Weight(Pounds)'] < 300)]

    df.reset_index(drop=True, inplace=True)
    print(f"Cleaned data: {len(df)} rows remaining.")
    return df

if __name__ == "__main__":
    df = load_data()
    df = clean_data(df)
    describe_data(df)
    plot_data(df)