import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(filepath_or_buffer='affairs.csv')
missing_values_count = df.isnull().sum()
print(missing_values_count)

# # Assuming your DataFrame is named 'df'
# affairs_distribution = df['affairs'].value_counts()

# # Plotting the pie chart
# affairs_distribution.plot(kind='pie', autopct='%1.1f%%')

# # Adding labels and title
# plt.title('Distribution of Affairs')
# plt.ylabel('')
# plt.legend(labels=['No Affair', 'Affair'])
# plt.show()


# -------------------------------------------

# # Assuming your DataFrame is named 'df'
# affairs_distribution = df['affairs'].value_counts()

# # Plotting the pie chart using DataFrame.plot().pie()
# affairs_distribution.plot.pie(autopct='%1.1f%%')

# # Adding labels and title
# plt.title('Distribution of Affairs')
# plt.ylabel('')
# plt.legend(labels=['No Affair', 'Affair'])
# plt.show()


#----------------------------------------------

# # Assuming your DataFrame is named 'df'
# # Round up 'yrs_married' column to integer
# df['yrs_married_rounded'] = df['yrs_married'].apply(lambda x: int(x))

# # Group the data by 'yrs_married_rounded' and count the occurrences of 'affairs' for each group
# affairs_distribution = df[df['affairs'] == 1].groupby('yrs_married_rounded')['affairs'].count()

# # Plotting the histogram
# affairs_distribution.plot(kind='bar')

# # Adding labels and title
# plt.title('Distribution of Affairs by Years Married')
# plt.xlabel('Years Married')
# plt.ylabel('Count')
# plt.show()


#----------------------------------------------------

# import pandas as pd
# import matplotlib.pyplot as plt

# # Assuming your DataFrame is named 'df'
# # Round up 'yrs_married' column to integer
# df['yrs_married_rounded'] = df['yrs_married'].apply(lambda x: int(x))

# # Group the data by 'yrs_married_rounded' and count the occurrences of 'affairs' for each group
# affairs_distribution = df.groupby(['yrs_married_rounded', 'affairs']).size().unstack(fill_value=0)

# # Plotting the stacked bar chart
# affairs_distribution.plot(kind='bar', stacked=True)

# # Adding labels and title
# plt.title('Distribution of Affairs by Years Married')
# plt.xlabel('Years Married')
# plt.ylabel('Count')
# plt.legend(['No Affair', 'Affair'])
# plt.show()

#----------------------------------------------------

# import pandas as pd
# import matplotlib.pyplot as plt

# # Assuming your DataFrame is named 'df'
# # Round up 'age' and 'yrs_married' columns to integers
# df['age_rounded'] = df['age'].apply(lambda x: int(x))
# df['yrs_married_rounded'] = df['yrs_married'].apply(lambda x: int(x))

# # Plotting the scatterplot
# plt.scatter(df['age_rounded'], df['yrs_married_rounded'])

# # Adding labels and title
# plt.title('Distribution of Age and Years Married')
# plt.xlabel('Age')
# plt.ylabel('Years Married')
# plt.show()


#----------------------------------------------------

# import pandas as pd
# import matplotlib.pyplot as plt

# Assuming your DataFrame is named 'df'
# Round up 'age' and 'yrs_married' columns to integers
df['age_rounded'] = df['age'].apply(lambda x: int(x))
df['yrs_married_rounded'] = df['yrs_married'].apply(lambda x: int(x))

# Count the number of elements for each combination of 'age_rounded' and 'yrs_married_rounded'
scatter_data = df.groupby(['age_rounded', 'yrs_married_rounded']).size().reset_index(name='count')

# Extract the x, y, and size values for the scatterplot
x = scatter_data['age_rounded']
y = scatter_data['yrs_married_rounded']
size = scatter_data['count']

# Plotting the scatterplot with size reflecting the count
plt.scatter(x, y, s=size)

# Adding labels and title
plt.title('Distribution of Age and Years Married')
plt.xlabel('Age')
plt.ylabel('Years Married')
plt.show()