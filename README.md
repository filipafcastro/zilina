# Hands-on Data Science: predicting bike traffic between Austria and Slovakia

## 💾 Data

[Open Data Bratislava](https://opendata.bratislava.sk/en/) provides freely available data on several topics, such as transportation, economy, politics, etc.

For this challenge in particular, we'll be using data aboutregarding the number of bike passes to Slovakia and Austria at the Berg. We'll be using data from [2016](https://opendata.bratislava.sk/en/dataset/show/cykloscitac-na-hradzi-berg-v-roku-), [2017](https://opendata.bratislava.sk/en/dataset/show/cykloscitac-na-hradzi-berg-v-roku-a), [2018](https://opendata.bratislava.sk/en/dataset/show/cykloscitac-na-hradzi-berg-v-roku-b) and [2019](https://opendata.bratislava.sk/en/dataset/show/cykloscitac-na-hradzi-berg-v-roku-do).

## 📚 Repository Structure
+ `data/traffic`: contains the traffic data from 2016 to 2019, extracted from [Open Data Bratislava](https://opendata.bratislava.sk/en/) 

+ `data/weather`: contains the weather historic data from 2016 to 2019, extracted from [meteostat](https://meteostat.net/en) 

+ `data/holidays`: contains public holidays in both [Austria](https://en.wikipedia.org/wiki/Public_holidays_in_Austria) and [Slovakia](https://en.wikipedia.org/wiki/Public_holidays_in_Slovakia), manually extracted from [Wikipedia](https://www.wikipedia.org/).

+ `etl_dataset.py`: merges all the provided data into a clean dataset: `Berg_bicycle_counter_2016_2019.csv`

+ `trafic_notraffic.ipynb`: jupyter notebook containing the proposed challenge.

## 💻 How to use it?

To work on the challenge, you'll simply need to:

+ download `trafic_notraffic.ipynb`
+ open `trafic_notraffic.ipynb` on [Google Colab](https://colab.research.google.com/)
+ upload `Berg_bicycle_counter_2016_2019.csv` to your Google Colab notebook.


