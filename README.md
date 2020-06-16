# Walmart-Store-Sales-Forecasting

### BUSINESS PROBLEM :

The objective is predicting store sales using historical markdown data. One challenge of modelling retail data is the need to make decisions based on limited history. If Christmas comes but once a year, so does the chance to see how stratigic decisions impacted the bottom line.

### DATA AVAILABILITY :

We are provided with historical sales for 45 Walmart stores located in different regions. Each store contains a number of departments, and you are tasked with predicting the department-wide sales for each store.

In addition Walmart runs several promotional markdown eventss throughout the years. These markdowns precede prominent holidays,the four largest of which are the Super Bowl, Labour Day, Thanksgiving, and Christmas. THe weeks including these holidays are weighted 5 times higher in the evaluation than non-holiday weeks. Part of challenge presented by this is modelling the effects of markdowns on these holiday weeks in the absence of complete/ideal historical data.

1) stores.csv : This file contains anonymized information about 45 stores, indicating the type and size of store.

2) train.csv : This is the historical training data, which covers to 2010-02-05 to 2012-10-26. Within file you will fing the following fields :

(a) Store - the store number.

(b) Dept - the department number.

(c) Date - the week.

(d) Weekly_Sales - sales for the given department in the given store.

(e) IsHoliday - whether the week is a special holiday week.

3) test.csv : The file is identical to train.csv, except we have withheld the Weekly_Sales. You must predict the sales for each triplet of store, department and date in this file.

4) features.csv : The file contains additional data related to the store, department, and regional activities for the given dates. It contains the following fields :

(a) Store -the store number.

(b) Date - the week.

(c) Temperature - average temperature in the region.

(d) Fuel_Price - cost of fuel in the region.

(e) MarkDown1-5 - anonymized data related to promotional markdowns that Walmart is running. MarkDown data is only available after Nov, 2011, and is not available for all stores all the time. Any missing value is marked with an NA.

(f)CPI - the consumer price index.

(g) Unemployment - the unemployment rate.

(h) IsHoliday - whether the week is a special holiday week.

