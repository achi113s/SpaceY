# IBM Data Science Professional Certificate Capstone Project

## "Winning the Space Race with Data Science" :rocket:

## Introduction :sunny:

This is the capstone project for the IBM Data Science Professional certificate program on Coursera. In this project, I will be applying many of the concepts that I have learned throughout the entire curriculum in order to complete a start to end data science project.

The premise of the project is this: I am working at a startup called Space Y, which is a competitor in the commercial space market. Our largest competitor is the familiar Space X, led by Elon Musk. One of the main reasons for Space X's success is the relative cheapness of their Falcon 9 rocket launches. The advertised price for a launch with their Falcon 9 rocket is approximately $67 million (as of December 2022). In comparison, other companies charge in the upper $100 millions.

One reason for the inexpensiveness of these launches is that the first stage of the rocket is reusable. The first stage is designed to be able to land itself on remote pads where the company can then recover it. However, sometimes the first stage is not recovered. There are times when the first stage crashes or is sacrificed due to mission parameters like payload, orbit, or the customer's needs. If we can determine if the first stage in a particular Falcon 9 launch will successfully land and be recovered, we can estimate the total cost of a launch. This information will be invaluable for Space Y stakeholders.

## Outline of Files :ledger:

1. Data Collection Part 1: In this notebook, I collect data on the Falcon 9 launches using the SpaceX REST API. I make further requests to the API with ID numbers retrieved in the first API call to construct a complete Pandas DataFrame.

2. Data Collection Part 2: Here I collect more data, but this time scraping data from a Wikipedia page on the Falcon 9 launches using BeautifulSoup. There is a fair amount of data cleaning and wrangling involved in this notebook.

3. Data Wrangling: Some quick analysis and exploration, but mostly the engineering of a feature called "Class" which is a categorical variable indicating whether a launch resulted in a failed (0) or successful (1) landing attempt.

4. Exploring Data with SQL: The data collected in the previous notebooks is loaded into a SQLite database and queried to gain some insight.

5. EDA with Visualizations: Using plots to do some exploratory data analysis.

6. Launch Sites Folium: Using the Folium library to do some analysis of the geographical features in the dataset. Where are the launch sites? Is there a correlation between launch site and landing success?

7. Dash Plotly Dashboard: A Python web app dashboard made using Plotly Dash. This dashboard showcases the proportion of successful landing attempts at each launch site and also shows a scatter plot of the relationship between rocket booster version, payload mass, and landing outcome. You can view the dashboard here: [PythonAnywhereDashboard](glat1957.pythonanywhere.com).


