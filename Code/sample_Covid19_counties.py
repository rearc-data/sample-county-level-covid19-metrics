import pandas as pd
covid_counties = pd.read_csv("./counties.csv")
covid_counties_100 = covid_counties.head(100)
covid_counties_100.to_csv("covid_counties_100.csv")
