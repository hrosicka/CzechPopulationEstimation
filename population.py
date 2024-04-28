# Import necessary libraries
import pandas as pd                             # Import pandas library for data manipulation
import os.path                                  # Import for file path manipulation
import matplotlib.pyplot as plt                 # Import matplotlib for plotting
from matplotlib.patches import Rectangle        # import Rectangle for legend and description


def plot_sp_pop_dpnd(df_czechia):
    """
    Plots the age dependency ratio (SP.POP.DPND) for the Czech Republic from the provided DataFrame.
    SP.POP.DPND = Age dependency ratio (% of working-age population)

    Args:
        df_czechia (pandas.DataFrame): A DataFrame containing data for the Czech Republic.
    """

    # Extract data for plotting
    x_sp_pop_dpnd = df_czechia.index.to_numpy()
    y_sp_pop_dpnd = df_czechia["SP.POP.DPND"].to_numpy() 

    # Create the plot
    fig, ax = plt.subplots()
    ax.stackplot(x_sp_pop_dpnd, y_sp_pop_dpnd, colors=["lightblue"])

    # Set plot limits and labels
    ax.set_xlim(min(x_sp_pop_dpnd), max(x_sp_pop_dpnd))
    ax.set_xticks([min(x_sp_pop_dpnd), '1975', '1990', '2005', '2020', '2035', max(x_sp_pop_dpnd)])
    ax.set_title("Age Dependency Ratio (% Of Working-Age Population)")

    # Add legend explaining the Age Dependency Ratio (more informative approach)
    text1 = "The Age Dependency Ratio compares dependents"
    text2 = "(<15 and >64) to the working-age population (15-64)."
    extra = Rectangle((0, 0), 1, 1, fc="w", fill=False, edgecolor='none', linewidth=0)
    plt.legend([extra, extra],[text1, text2], loc='lower left', title='Legend')

    # Display the plot
    plt.show()


def plot_sp_pop_dpnd_ol(df_czechia):
    """
    Plots the old-age dependency ratio (SP.POP.DPND.OL) for the Czech Republic from the provided DataFrame.
    SP.POP.DPND.OL = Age dependency ratio, old

    Args:
        df_czechia (pandas.DataFrame): A DataFrame containing data for the Czech Republic.
    """

    # Extract data for plotting the old-age dependency ratio
    x_sp_pop_dpnd_ol = df_czechia.index.to_numpy()
    y_sp_pop_dpnd_ol = df_czechia["SP.POP.DPND.OL"].to_numpy() 

    # Create the plot
    fig, ax = plt.subplots()
    ax.stackplot(x_sp_pop_dpnd_ol, y_sp_pop_dpnd_ol, colors=["pink"])

    # Set plot limits and labels
    ax.set_xlim(min(x_sp_pop_dpnd_ol), max(x_sp_pop_dpnd_ol))
    ax.set_xticks([min(x_sp_pop_dpnd_ol), '1975', '1990', '2005', '2020', '2035', max(x_sp_pop_dpnd_ol)])
    ax.set_title("Age dependency ratio, old")

    # Add informative legend using Rectangle for aesthetics
    text1 = "Old-age dependency ratio shows how many people > 64"
    text2 = "rely on every 100 working-age adults (15-64)."
    extra = Rectangle((0, 0), 1, 1, fc="w", fill=False, edgecolor='none', linewidth=0)
    plt.legend([extra, extra],[text1, text2], loc='lower left', title='Legend')

    # Display the plot
    plt.show()


def plot_sp_pop_dpnd_yg(df_czechia):
    """
    Plots the young dependency ratio (SP.POP.DPND.YG) for the Czech Republic from the provided DataFrame.
    SP.POP.DPND.YG = Age dependency ratio, young
    
    Args:
        df_czechia (pandas.DataFrame): A DataFrame containing data for the Czech Republic.
    """

    # Extract data for plotting the young dependency ratio
    x_sp_pop_dpnd_yg = df_czechia.index.to_numpy()
    y_sp_pop_dpnd_yg = df_czechia["SP.POP.DPND.YG"].to_numpy() 

    # Create the plot
    fig, ax = plt.subplots()
    ax.stackplot(x_sp_pop_dpnd_yg, y_sp_pop_dpnd_yg, colors=["lightgreen"])

    # Set plot limits and labels
    ax.set_xlim(min(x_sp_pop_dpnd_yg), max(x_sp_pop_dpnd_yg))
    ax.set_xticks([min(x_sp_pop_dpnd_yg), '1975', '1990', '2005', '2020', '2035', max(x_sp_pop_dpnd_yg)])
    ax.set_title("Age dependency ratio, young")

    # Add informative legend using Rectangle for aesthetics
    text1 = "Young dependency ratio shows how many < 15"
    text2 = "rely on every 100 working-age adults (15-64)."
    extra = Rectangle((0, 0), 1, 1, fc="w", fill=False, edgecolor='none', linewidth=0)
    plt.legend([extra, extra],[text1, text2], loc='lower left', title='Legend')

    # Display the plot
    plt.show()


def main():
    """
    Reads all population data, selects data for the Czech Republic, calculates dependency ratios, and generates plots.
    """

    # Get the path to the CSV file (assuming it's in the same directory)
    current_dir = os.path.abspath(os.getcwd())
    filepath = os.path.join(current_dir, "Population-EstimatesEXCEL.csv")

    # Read the CSV data into a pandas DataFrame
    df = pd.read_csv((filepath), index_col='Indicator Code')

    # Filter data for the Czech Republic
    czechia_condition = df['Country Code'] == 'CZE'
    df_czechia = df[czechia_condition]

    # Remove unnecessary columns
    del df_czechia['Country Name']
    del df_czechia['Country Code']
    del df_czechia['Indicator Name']

    # Transpose the DataFrame for easier access (optional, depending on data structure)
    df_czechia = df_czechia.T

    # Generate plots for different dependency ratios
    plot_sp_pop_dpnd(df_czechia)        # Overall dependency ratio
    plot_sp_pop_dpnd_ol(df_czechia)     # Old-age dependency ratio
    plot_sp_pop_dpnd_yg(df_czechia)     # Young dependency ratio


if __name__ == "__main__":
    main()