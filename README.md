# FIFA World Cup Dashboard

### Premise

We set out to create a dashboard that would display a number of graphs and statistics on past Fifa World Cup Series. These ranged from the 1994 World Cup, up until the qualifying games of 2022. Data was taken both from a data set on Kaggle.com, as well as scraped data from Wikipedia

### Data Sources

Fifa World Cup 1993-2022  
Kaggle  
https://www.kaggle.com/datasets/brenda89/fifa-world-cup-2022?resource=download 

Fifa World Cup Squads 1994-2018  
Wikipedia (Scraped)  
https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_squads 
https://en.wikipedia.org/wiki/2014_FIFA_World_Cup_squads 
https://en.wikipedia.org/wiki/2010_FIFA_World_Cup_squads 
https://en.wikipedia.org/wiki/2006_FIFA_World_Cup_squads 
https://en.wikipedia.org/wiki/2002_FIFA_World_Cup_squads 
https://en.wikipedia.org/wiki/1998_FIFA_World_Cup_squads 
https://en.wikipedia.org/wiki/1994_FIFA_World_Cup_squads 

### Code Explanation

Data from Wikipedia was scraped using python and BeautifulSoup.
All data sets were tydied and formatted using Python, primarily with the use of Pandas package.

Data tables were added to a sqlite database using Python and SQLAlchemy. Three data tables were made including country data, EA/Fifa rank data and squad data. Each table contained a varying number of rows, as well as a primary key. Each table was distinctly different, so no foreign keys were necessary.



