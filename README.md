# Walmart-Store-Sales-Forecasting

## Table of Content
  * [Directory Tree](#directory-tree)
  * [BUSINESS PROBLEM](#business-problem)
  * [DATA AVAILABILITY](#data-availability)
  * [ATTACK CLASS](#attack-class)
  * [How to Use](#how-to-use)
  * [LICENSE](#license)
  
  ### Directory Tree

```
├── data
│   ├── features.csv
│   ├── stores.csv
│   ├── test.csv
│   ├── train.csv
├── results
│   ├── 2020-06-16 20_13_25-Settings.png
│   ├── 2020-06-16 20_14_05-Settings.png
├── static
│   ├── style.css
├── templates
│   ├── index.html
├── app.py
├── corrm.csv
├── Dockerfile
├── model.pkl
├── Walmart Store Sales Forecasting.ipynb
├── num_summary.csv
├── all_features.csv
├── requirements.txt
├── LICENSE
├── Procfile
├── README.md
```

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

### How to Use

Just follow 3 simple steps :

1. Go to project website link https://wssf.herokuapp.com/ .<br>

2. Fill the form as shown below :<br><br>

![](https://github.com/vicky60629/Walmart-Store-Sales-Forecasting/blob/master/results/2020-06-16%2020_13_25-Settings.png)<br>

3. Then Click on Predict and you get the predicted attack class .<br><br>

![](https://github.com/vicky60629/Walmart-Store-Sales-Forecasting/blob/master/results/2020-06-16%2020_14_05-Settings.png)<br>

**If you face any problem :** email me at *vg60629@gmail.com*

### LICENSE

[MIT License](https://github.com/vicky60629/Walmart-Store-Sales-Forecasting/blob/master/LICENSE)

Copyright (c) 2020 Vicky Gupta

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
