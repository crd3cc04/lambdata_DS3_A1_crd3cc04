# Creating a list from dataframe and adding it to dataframe
import pandas as pd
df = pd.DataFrame({'wk_birthday': pd.date_range('2020-09-20', periods=7),
                   'color_day': ['blue', 'red', 'yellow', 'organge', 'white', 'black', 'teal'],
                   'num_of_day': ['2', '5', '8', '1', '4', '10', '7']
                   })
print(df)

# Actual list going to use....
df = df.head()
print(df.head())

from my_lambdata1.my_mod import birthday_list

happy = birthday_list(df)
print(happy)