import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

y = [90,80,85,75,65,60,5]
x = ['ML & DL', 'Django', 'HTML5', 'JavaScript', 'CSS3', 'Bootstrap', 'VUE.JS']
colours = ['#39d084', '#30a5dc', '#7447f0', '#ee742b', '#d0ce39', '#ee2bbd', 'red']
'''
plt.barh(x,y, color=colours, height=0.5)
for i in range(len(y)):
    plt.annotate(str(y[i]), xy=(x[i],y[i]), ha='center', va='bottom')
plt.show()
'''
plt.pie(y, labels=x, labeldistance=0.48, colors=colours,shadow=True)
plt.title('Nwovu Sunday Skills Chart', fontsize=24)
#plt.legend(title='Skills', bbox_to_anchor=(1, 1))
plt.savefig('skillspie', transparent=True)
plt.show()
'''
# Bring some raw data.
frequencies = y.copy()

# In my original code I create a series and run on that,
# so for consistency I create a series from the list.
freq_series = pd.Series(frequencies)
#freq_series = np.array(freq_series)

x_labels = x.copy()

# Plot the figure.
plt.figure(figsize=(7, 7))
ax = freq_series.plot(kind='bar', color=colours, width=0.4)
ax.set_title('Skills in Percentage')
ax.set_xlabel('Skills')
ax.set_ylabel('Percentage')
ax.set_xticklabels(x_labels)


def add_value_labels(ax, spacing=5):
    """Add labels to the end of each bar in a bar chart.

    Arguments:
        ax (matplotlib.axes.Axes): The matplotlib object containing the axes
            of the plot to annotate.
        spacing (int): The distance between the labels and the bars.
    """

    # For each bar: Place a label
    for rect in ax.patches:
        # Get X and Y placement of label from rect.
        y_value = rect.get_height()
        x_value = rect.get_x() + rect.get_width() / 2

        # Number of points between bar and label. Change to your liking.
        space = spacing
        # Vertical alignment for positive values
        va = 'bottom'

        # If value of bar is negative: Place label below bar
        if y_value < 0:
            # Invert space to place label below
            space *= -1
            # Vertically align label at top
            va = 'top'

        # Use Y value as label and format number with one decimal place
        label = "{:.1f}".format(y_value)

        # Create annotation
        ax.annotate(
            label,                      # Use `label` as label
            (x_value, y_value),         # Place label at end of the bar
            xytext=(0, space),          # Vertically shift label by `space`
            textcoords="offset points", # Interpret `xytext` as offset in points
            ha='center',                # Horizontally center label
            va=va)                      # Vertically align label differently for
                                        # positive and negative values.


# Call the function above. All the magic happens there.
add_value_labels(ax)

plt.savefig("skillsbar.png")
'''