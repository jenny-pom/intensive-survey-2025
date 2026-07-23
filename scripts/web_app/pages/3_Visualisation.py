import streamlit as st
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import matplotlib.dates as mdates

st.set_page_config(
    page_title="Visualisation of Intensive Survey 2025", 
    layout="wide",
    initial_sidebar_state="expanded"
)
st.title("Visualisation of Intensive Survey 2025")

df = pd.read_csv('../../data/processed/CLEAN_forJenny_IntensiveSurvey2025.csv') # Read the CSV file into a DataFrame
df['end'] = pd.to_datetime(df['end']) # Convert date column to datetime object
df.set_index('end', inplace=True) # Set the date column as the index of the DataFrame

st.subheader("Q1: How does the flowering count and fruit count change along the season?")
st.markdown("""
            I do an intital analysis where I collapses all individual plants into a single daily total,
            where all flower counts are summed together and all fruit counts are summed together for 
            each day the survey is performed and plotted against time. This is a good first step to 
            see the overall seasonal trend of flower and fruits counts (combined) and observe outliers.

            Note: The (initial) drop in total flower count that was observed on the 5th to 6th of 
            June is due to a gap in the data where almost all plants are counted as (NA). 
            This occured because we expanded the number of observed individuals that day and 
            only recorded location and gave ID tags. Thi part is now corrected. The dip in fruit count observed on the 
            4th of July could potentially be explained by a rotation in the volouteers performing 
            the intensive servey. 
            """)
    
# Group by date index and calculate the sum for each day
daily_totals = df.groupby(df.index)[['Estim.Flowers.Nr', 'Estim.Fruits.Nr']].sum()

# Set up a slightly wider plot
fig, ax = plt.subplots(figsize=(15, 7))

ax.plot(daily_totals.index, daily_totals['Estim.Flowers.Nr'], color='#66c2a5', linewidth=2.5, marker='o', label='Total Flowers')
ax.plot(daily_totals.index, daily_totals['Estim.Fruits.Nr'], color='#fc8d62', linewidth=2.5, marker='s', label='Total Fruits')

# Tell the X-axis to place a tick mark on every third day
ax.xaxis.set_major_locator(mdates.DayLocator(interval=3))
# Format how the date looks
ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
# Rotate the text 90 degrees
plt.xticks(rotation=90, fontsize=9) 

# Customize labels and design
plt.title('Seasonal Shift: Total Flower Counted vs. Total Fruit Counted', fontsize=15, pad=15)
plt.xlabel('Date of Collection', fontsize=12, labelpad=15)
plt.ylabel('Total Count (All Plants Combined)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.4)
plt.legend(fontsize=11, loc='upper right')
plt.tight_layout()

# Tell Streamlit to render the figure object directly onto the page
st.pyplot(fig)

###-------------Row2--------------###
st.write("---") # Visual divider line
###-------------------------------###

st.subheader("Q2: How does flowering late in season effect the fruit yield?")
st.markdown("""
            I start by plotting the data as box plots to see how the flower 
            count vs fruit counts change over the season for different months. 
            
            **Key Insights:**
            * May: Dominated by heavy vegetative/flowering investment.
            * June/July: Flower production tapers off as energy shifts entirely into fruit maturation.
            * Outliers: Individual plants showing extremely high yields highlight top-performing genetic variants.       
            """)

df_reset = df.reset_index() # Reread the datafile and reset the indexing
df_reset['Month'] = df_reset['end'].dt.month_name()
# Reshape data from wide to long format
df_melted = df_reset.melt(
    id_vars=['Month', 'PlantID'], 
    value_vars=['Estim.Flowers.Nr', 'Estim.Fruits.Nr'], 
    var_name='Count Type', 
    value_name='Count'
)
# Clean up label text to make it look nicer
df_melted['Count Type'] = df_melted['Count Type'].map({
    'Estim.Flowers.Nr': 'Flowers',
    'Estim.Fruits.Nr': 'Fruits'
})
# Establish chronological sorting for the seasonal survey 
month_order = ['May', 'June', 'July'] 
df_melted['Month'] = pd.Categorical(df_melted['Month'], categories=month_order, ordered=True)

# Set up figure explicitly
fig2, ax2 = plt.subplots(figsize=(10, 6))

# Generate the boxplot
sns.boxplot(
    data=df_melted, 
    x='Month', 
    y='Count', 
    hue='Count Type', 
    palette='Set2',
    ax=ax2
)

ax2.legend(title='Count Type', loc='upper right') 
ax2.set_title('Flowering vs. Fruiting Counts Across Months', fontsize=14)
ax2.set_xlabel('Month of Data Collection', fontsize=12)
ax2.set_ylabel('Count', fontsize=12)

plt.tight_layout()
# Render explicitly inside Streamlit
st.pyplot(fig2)

###-------------Row3--------------###
st.write("---") # Visual divider line
###-------------------------------###
st.subheader("Q3: Does plants with flowers later in the seeason have a higher fruit yield?")

st.markdown("""
            I isolate the subset of plants exhibiting late-season flowering 
            (defined as plants with active flower counts in July) and plot them against the max yield of fruits. 
            We compare these late-season flowering plants to plants where no flowers were observed in July.
            """)

# Isolate July data to identify the plant groups (Month == 7)
july_data = df[df.index.month == 7]
# Calculate total July flowers per plant
july_flowers = july_data.groupby('PlantID')['Estim.Flowers.Nr'].sum()
# Group A: Plants that flowered in July (Total > 0)
late_bloomers_ids = july_flowers[july_flowers > 0].index.tolist()
# Group B: Plants with zero flowers in July
no_july_flowers_ids = july_flowers[july_flowers == 0].index.tolist()
# Find the max fruit count across all months per plant
max_fruit_per_plant = df.groupby('PlantID')['Estim.Fruits.Nr'].max().reset_index()

# Assign each plant to its respective group
def assign_group(plant_id):
    if plant_id in late_bloomers_ids:
        return 'Late Bloomers (July Flowers)'
    elif plant_id in no_july_flowers_ids:
        return 'Standard Cycle (No July Flowers)'
    return 'Other'

max_fruit_per_plant['Group'] = max_fruit_per_plant['PlantID'].apply(assign_group)

# Filter out unclassified entries
comparison_df = max_fruit_per_plant[max_fruit_per_plant['Group'] != 'Other']

fig3, ax3 = plt.subplots(figsize=(10, 6))

sns.boxplot(data=comparison_df, x='Group', y='Estim.Fruits.Nr', palette=['#66c2a5', '#fc8d62'], width=0.4, ax=ax3)

sns.stripplot(data=comparison_df, x='Group', y='Estim.Fruits.Nr', color='black', alpha=0.2, size=5, jitter=0.1, ax=ax3)

ax3.set_title('Effect of Late-Season Flowering on Max Fruit Yield', fontsize=14, pad=15)
ax3.set_xlabel('Plant Grouping (July Behavior)', fontsize=12)
ax3.set_ylabel('Maximum Fruit Yield Attained', fontsize=12)
ax3.grid(axis='y', linestyle='--', alpha=0.4)
plt.tight_layout()
st.pyplot(fig3)

###-------------Row4--------------###
st.write("---") # Visual divider line
###-------------------------------###
# Process the efficiency data
flower_total = df.groupby('PlantID')[['Estim.Flowers.Nr']].sum()
seed_max = df.groupby('PlantID')[['Estim.Fruits.Nr']].max()

# Merge metrics together
plant_max = pd.merge(flower_total, seed_max, on='PlantID')

# Calculate conversion percentage safely avoiding division-by-zero errors
plant_max['Success_Percentage'] = np.where(
    plant_max['Estim.Flowers.Nr'] > 0,
    (plant_max['Estim.Fruits.Nr'] / plant_max['Estim.Flowers.Nr']) * 100,
    0
)

# Sort from most to least efficient
plant_max = plant_max.sort_values(by='Success_Percentage', ascending=False).reset_index()
avg_pct = plant_max['Success_Percentage'].mean()

st.subheader("Q4: Does plants with high flower count on average have a higher yield of fruits?")
st.markdown("""
            To visualize the efficiency of flower to fruit ratio, I extract the max count of 
            number of fruits and the total number of flowers counted for each plant ID. 
            I then score each plant as the percentage of max number of fruits divided by 
            total number of flowers. 

            $$\\text{Efficiency Score} = \\left( \\frac{\\text{Max Fruits}}{\\text{Total Flowers}} \\right) \times 100$$
            
            This score is then what I use to range each plant.
            """)

# Showcase the calculated average as a main widget metric
st.metric(label="Population Average Peak Success", value=f"{avg_pct:.1f}%")


# Set up figure explicitly
fig4, ax4 = plt.subplots(figsize=(13, 6))

# Generate the sorted bar plot
sns.barplot(
    data=plant_max, 
    x='PlantID', 
    y='Success_Percentage', 
    color='#2b8cbe',     
    edgecolor='none',
    ax=ax4
)

# Add horizontal structural reference lines
ax4.axhline(avg_pct, color='red', linestyle='--', linewidth=1.5, 
            label=f'Avg Peak Success ({avg_pct:.1f}%)')
ax4.axhline(100.0, color='gray', linestyle=':', linewidth=1.2, label='100% Max Conversion')

# Format Y-axis directly into percentages
ax4.yaxis.set_major_formatter(mtick.PercentFormatter())

# Styling and adjustments
ax4.set_title('Peak Fruit Success Rate (%) \n(Max Fruits / Total Flowers per Individual)', fontsize=14, pad=15)
ax4.set_xlabel('Individual Plants (Ranked from Most to Least Efficient)', fontsize=12)
ax4.set_ylabel('Peak Conversion Efficiency (%)', fontsize=12)

# Clean up empty spaces and axis markers
ax4.set_xticks([]) 
ax4.grid(axis='y', linestyle='--', alpha=0.4)
ax4.legend(fontsize=11, loc='upper right')
ax4.set_ylim(0, 110)

plt.tight_layout()
# Render explicitly inside Streamlit
st.pyplot(fig4)