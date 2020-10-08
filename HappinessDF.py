# imports
import pandas as pd

# files for each specific year
df_2015 = pd.read_csv (r'/Users/hayleykisiel/Desktop/Happiness/2015.csv', \
                       usecols= ['Country','Region','Happiness Rank','Happiness Score'])
df_2016 = pd.read_csv (r'/Users/hayleykisiel/Desktop/Happiness/2016.csv', \
                       usecols= ['Country','Happiness Rank', 'Happiness Score'])
df_2017 = pd.read_csv (r'/Users/hayleykisiel/Desktop/Happiness/2017.csv', \
                       usecols= ['Country','Happiness.Rank', 'Happiness.Score','Family','Dystopia.Residual'])
df_2018 = pd.read_csv (r'/Users/hayleykisiel/Desktop/Happiness/2018.csv', \
                       usecols= ['Overall rank','Country or region','Score'])
df_2019 = pd.read_csv (r'/Users/hayleykisiel/Desktop/Happiness/2019.csv', \
                       usecols= ['Overall rank','Country or region','Score',\
                        'GDP per capita','Social support','Healthy life expectancy',\
                        'Freedom to make life choices','Generosity','Perceptions of corruption'])

# merge data frames into one
df = df_2015.merge(df_2016, on='Country')
df = df.merge(df_2017, on='Country')
df = df.merge(df_2018, left_on='Country', right_on='Country or region')
df = df.merge(df_2019, on='Country or region')

# rename columns
df.rename(columns={'Happiness Rank_x': 'Rank 2015','Happiness Score_x': 'Happiness Score 2015',\
    'Happiness Rank_y': 'Rank 2016','Happiness Score_y': 'Happiness Score 2016',\
    'Happiness.Rank': 'Rank 2017','Happiness.Score': 'Happiness Score 2017',\
    'Dystopia.Residual': 'Dystopia Residual','Overall rank_x': 'Rank 2018',\
    'Score_x': 'Happiness Score 2018','Overall rank_y': 'Rank 2019',\
    'Score_y': 'Happiness Score 2019'}, inplace=True)
    
# rearrange columns
df = df[['Country','Region','Happiness Score 2015','Happiness Score 2016',\
        'Happiness Score 2017','Happiness Score 2018','Happiness Score 2019','Rank 2015','Rank 2016'\
        ,'Rank 2017','Rank 2018','Rank 2019','Family','GDP per capita','Social support',\
        'Healthy life expectancy','Freedom to make life choices','Generosity',\
        'Perceptions of corruption','Dystopia Residual']]

# highest 10 happiness scores for 2019
print(df.nsmallest(10,['Rank 2019'])) 
    
# lowest 10 happiness scores for 2019
print(df.nlargest(10,['Rank 2019']))

# export csv

df.to_csv(r"/Users/hayleykisiel/Desktop/HappinessCSV.csv", index = False, sep=',', encoding = 'utf-8')
