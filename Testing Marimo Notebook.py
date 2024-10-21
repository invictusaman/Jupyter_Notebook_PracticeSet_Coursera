import marimo

__generated_with = "0.9.8"
app = marimo.App(width="medium")


@app.cell
def __():
    import pandas as pd
    return (pd,)


@app.cell
def __():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def __(mo):
    mo.md(
        r"""
        # Test

        ---
        This is another markdown file. Does markdown hides?

        **bold** or *italics* 

        ----
        """
    )
    return


@app.cell
def __(pd):
    df = pd.read_csv('sample_data.csv')
    return (df,)


@app.cell
def __(df):
    print(df.shape)
    return


@app.cell(hide_code=True)
def __(mo):
    mo.md("""Printing first few rows of the dataset.""")
    return


@app.cell
def __(df):
    # Display the first few rows of the dataset
    print("First few rows of the dataset:")
    df.head()
    return


@app.cell
def __(df):
    print(df.shape)
    return


@app.cell
def __():
    # Visualizations (uncomment these if using in a Jupyter Notebook or an environment that supports plotting)
    import matplotlib.pyplot as plt
    import seaborn as sns

    # # Scatter plot for Spending Score vs. Annual Income
    # plt.figure(figsize=(8, 5))
    # plt.scatter(df['Annual_Income'], df['Spending_Score'], alpha=0.7, color='blue')
    # plt.title('Spending Score vs. Annual Income')
    # plt.xlabel('Annual Income')
    # plt.ylabel('Spending Score')
    # plt.show()

    # # Heatmap for correlation matrix
    # plt.figure(figsize=(8, 5))
    # sns.heatmap(df.corr(), annot=True, cmap='coolwarm', vmin=-1, vmax=1)
    # plt.title('Correlation Matrix Heatmap')
    # plt.show()
    return plt, sns


@app.cell
def __(df, plt):
    # Histogram for age distribution
    plt.figure(figsize=(8, 5))
    plt.hist(df['Age'], bins=10, color='skyblue', edgecolor='black')
    plt.title('Age Distribution')
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    plt.show()
    return


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
