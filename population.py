# Import necessary libraries
import pandas as pd                             # Import pandas library for data manipulation
import os.path                                  # Import for file path manipulation
import matplotlib.pyplot as plt                 # Import matplotlib for plotting
from matplotlib.patches import Rectangle        # Import Rectangle for legend and description
import numpy as np                              # Import numpy for numerical operations

def annot_max(x,y, color, textcolor, ax=None):
    """
    Annotates the maximum value in a data array (`y`) value on a Matplotlib plot (`ax`).

    Parameters:
        x (numpy.ndarray): The x-axis data array (e.g., years).
        y (numpy.ndarray): The y-axis data array (corresponding values).
        color (str): The color for the annotation box and arrow.
        textcolor (str): The color for the annotation text.
        ax (matplotlib.axes._axes.Axes, optional): The Matplotlib axes object for the plot.
            If not provided, the current axes (plt.gca()) is used.

    Returns:
        None
    """
    # Find the index of the maximum value in y
    xmax = x[np.argmax(y)]

    # Extract the maximum value from y
    ymax = y.max()

    # Format the annotation text including the year with the maximum value
    # and the corresponding age dependency ratio
    text= "MAXIMUM IN YEAR {}\nAge Dependency Ratio {:.3f}".format(xmax, ymax)

    # Check if an axes object (ax) is provided. If not, retrieve the current axes.
    if not ax:
        ax=plt.gca()
    
    # Define properties for the annotation box and arrow
    bbox_props = dict(color=color, boxstyle="round,pad=0.9")
    arrowprops=dict(color=color, arrowstyle="->")

    # Set up keyword arguments for the annotation
    kw = dict(color=textcolor, 
              xycoords='data',
              textcoords="axes fraction",
              arrowprops=arrowprops,
              bbox=bbox_props,
              ha="right",
              va="top")
    
    # Calculate the y-text position based on the maximum value (ymax)
    ytext = ymax/100 + 0.25

    # Adjust the horizontal text position (xytext) based on the year (xmax)
    if int(xmax) > 1990:
        xytext = (0.9, ytext)  # Place text at the right side for better readability
    else:
        xytext = (0.5, ytext)  # Center the text for years before 1991

    # Add the annotation with text and an arrow pointing to the maximum data point
    ax.annotate(text, xy=(xmax, ymax), xytext=xytext, **kw)


def annot_min(x,y, color, textcolor, ax=None):
    """
    Annotates the minimum value in a data array (`y`) on a Matplotlib plot (`ax`).

    Parameters:
        x (numpy.ndarray): The x-axis data array (e.g., years).
        y (numpy.ndarray): The y-axis data array (corresponding values).
        color (str): The color for the annotation box and arrow.
        textcolor (str): The color for the annotation text.
        ax (matplotlib.axes._axes.Axes, optional): The Matplotlib axes object for the plot.
            If not provided, the current axes (plt.gca()) is used.

    Returns:
        None
    """

    # Find the index of the minimum value in y
    xmin = x[np.argmin(y)]

    # Extract the minimum value from y
    ymin = y.min()

    # Format the annotation text including the year with the minimum value
    # and the corresponding age dependency ratio
    text= "MINIMUM IN YEAR {}\nAge Dependency Ratio {:.3f}".format(xmin, ymin)

    # Check if an axes object (ax) is provided. If not, retrieve the current axes.
    if not ax:
        ax=plt.gca()

    # Define properties for the annotation box and arrow
    bbox_props = dict(color=color, boxstyle="round,pad=0.9")
    arrowprops=dict(color=color, arrowstyle="->")

    # Set up keyword arguments for the annotation
    kw = dict(color=textcolor,
              xycoords='data',
              textcoords="axes fraction",
              arrowprops=arrowprops,
              bbox=bbox_props,
              ha="right",
              va="top")
    
    # Calculate the y-text position based on the minimum value (ymin)
    ytext = ymin/100 + 0.30

    # Adjust the horizontal text position (xytext) based on the year (xmin)
    if int(xmin) > 2005:
        xytext = (0.9, ytext)  # Place text at the right side for better readability
    else:
        xytext = (0.5, ytext)  # Center the text for years before 2006

    # Add the annotation with text and an arrow pointing to the minimum data point
    ax.annotate(text, xy=(xmin, ymin), xytext=xytext, **kw)



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
    ax.stackplot(x_sp_pop_dpnd, y_sp_pop_dpnd, colors=["#E85F5C"])

    # Set plot limits and labels
    ax.set_xlim(min(x_sp_pop_dpnd), max(x_sp_pop_dpnd))
    ax.set_xticks([min(x_sp_pop_dpnd), '1975', '1990', '2005', '2020', '2035', max(x_sp_pop_dpnd)])
    ax.set_ylim(0, 100)
    ax.set_title("Age Dependency Ratio (% Of Working-Age Population)")

    # Add legend explaining the Age Dependency Ratio (more informative approach)
    text1 = "The Age Dependency Ratio compares dependents"
    text2 = "(<15 and >64) to the working-age population (15-64)."
    extra = Rectangle((0, 0), 1, 1, fc="w", fill=False, edgecolor='none', linewidth=0)
    plt.legend([extra, extra],[text1, text2], loc='lower left')

    annot_max(x_sp_pop_dpnd, y_sp_pop_dpnd, "#1D0200", "white")
    annot_min(x_sp_pop_dpnd, y_sp_pop_dpnd, "#5A1807", "white")

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
    ax.stackplot(x_sp_pop_dpnd_ol, y_sp_pop_dpnd_ol, colors=["#932F6D"])

    # Set plot limits and labels
    ax.set_xlim(min(x_sp_pop_dpnd_ol), max(x_sp_pop_dpnd_ol))
    ax.set_xticks([min(x_sp_pop_dpnd_ol), '1975', '1990', '2005', '2020', '2035', max(x_sp_pop_dpnd_ol)])
    ax.set_ylim(0, 100)
    ax.set_title("Age dependency ratio, old")

    # Add informative legend using Rectangle for aesthetics
    text1 = "Old-age dependency ratio shows how many people > 64"
    text2 = "rely on every 100 working-age adults (15-64)."
    extra = Rectangle((0, 0), 1, 1, fc="w", fill=False, edgecolor='none', linewidth=0)
    plt.legend([extra, extra],[text1, text2], loc='lower left')

    annot_max(x_sp_pop_dpnd_ol, y_sp_pop_dpnd_ol, "#420039", "white")
    annot_min(x_sp_pop_dpnd_ol, y_sp_pop_dpnd_ol, "#25171A", "white")


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
    ax.stackplot(x_sp_pop_dpnd_yg, y_sp_pop_dpnd_yg, colors=["#7B904B"])
 
    # Set plot limits and labels
    ax.set_xlim(min(x_sp_pop_dpnd_yg), max(x_sp_pop_dpnd_yg))
    ax.set_xticks([min(x_sp_pop_dpnd_yg), '1975', '1990', '2005', '2020', '2035', max(x_sp_pop_dpnd_yg)])
    ax.set_ylim(0, 100)
    ax.set_title("Age dependency ratio, young")

    # Add informative legend using Rectangle for aesthetics
    text1 = "Young dependency ratio shows how many < 15"
    text2 = "rely on every 100 working-age adults (15-64)."
    extra = Rectangle((0, 0), 1, 1, fc="w", fill=False, edgecolor='none', linewidth=0)
    plt.legend([extra, extra],[text1, text2], loc='lower left')

    annot_max(x_sp_pop_dpnd_yg, y_sp_pop_dpnd_yg, "#273B09", "white")
    annot_min(x_sp_pop_dpnd_yg, y_sp_pop_dpnd_yg, "#393E41", "white")

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