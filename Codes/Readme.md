## Brief Description of Various Parts of the Code

- EDF_convert.py\
Python code that converts PSG and Hypnograms to dataframes and merges both sets to create a csv file with x values and the labels

- csv_aggregate.scala\
Spark code that takes the CSVs generated from conversion and aggregates every 300 data points to create tensors in required format. This code was run from spark-shell for each individual reading

- eda.scala\
Spark code that access all aggregated data to carry out exploratory data analysis.This code was run from spark-shell for each individual reading

- Aggregated_RNN_CNN.ipynb\
Python notebook to run RNN,CNN models. The code also integrates the aggregate files output by csv_aggregate.scala.(While spark would be an easier platform to integrate the files, the combined csv was about 10GB which made it impossible to upload on Google Drive and access it all at once through Google Colab. So we opted to integrate again using python in Google Colab)

- Aggregated_CRNN (1).ipynb\
Python notebook similar to one above to run RNN,CNN models
