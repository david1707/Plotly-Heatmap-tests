# What is this about

Just testing the Python's Plotly library with the Heatmap graph.

## How can I make it work?

Run the file passing one argument as the name of the .csv file you want to read. In this example, a sample file was provided with the weekly temperatures (and more) from Benidorm, Valencian Country.

This is one row example:

Year,Month,Day,Hour,Minute,Temperature,Relative Humidity,Sunshine Duration,Wind Speed,Wind Direction
2018,11,18,00,00,12.77,84.00,0.00,13.08,7.91

If you want to use your own .csv, use this as a template, but with 'Day', 'Hour' and 'Temperature' is enough. Keep the file in the same folder.

How to run the code:

`python heatmap_city.py CITYNAME`

It will search for CITYNAME.csv (If not, it defaults to Benidorm.csv, file included) and in case it will find it, it creates a Heatmap like this one:

![Benidorm HeatMap](https://i.imgur.com/27iDE2d.jpg)
