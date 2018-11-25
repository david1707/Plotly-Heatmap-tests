# What is this about

Just testing the Python's Plotly library with the Heatmap graph.

## How can I make it work?

Run the file passing two arguments, the first as the name of the .csv file you want to read and the second one as the field you want to check. In this example, a sample file was provided with the weekly temperatures, Wind Speed, etc from Benidorm, Valencian Country.

This is one row example:

Year,Month,Day,Hour,Minute,Temperature,Humidity,SunshineDuration,WindSpeed,WindDirection
2018,11,18,00,00,12.77,84.00,0.00,13.08,7.91

If you want to use your own .csv, use this one as template, but 'Day', 'Hour' and 'Temperature' columns are enough. Keep the file at the root.

## How to run the code:

`python heatmap_city.py CITYNAME FIELD`

Example:

`python heatmap_city.py Benidorm Temperature`

It will look for Benidorm.csv (name + '.csv') and, if the file exists, will map the Temperature field creating this website:
![Benidorm HeatMap](https://i.imgur.com/27iDE2d.jpg)
