#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
import pandas as pd

enron_data = pickle.load(open("final_project/final_project_dataset.pkl", "r"))

# How many data points (people) are in the dataset?
poi = list(enron_data.keys())
print(len(poi))

# For each data point (person) how many features are available?
count_features = 0
for k, v in enron_data.items():
    if len(v) > count_features:
        count_features = len(v)
print(count_features)

# How many POIs are in the dataset?
# data[person_name]["poi"]==1
count_poi = 0
for k, v in enron_data.items():
    if v["poi"] == 1:
        count_poi += 1
print(count_poi)

# What is the total value of the stock belonging to James Prentice?
fpj = enron_data["PRENTICE JAMES"]
spj = pd.Series(fpj)
print(spj)
print(fpj["total_stock_value"])

# How many email messages do we have from Wesley Colwell to persons of interest?
fcl = enron_data["COLWELL WESLEY"]
scw = pd.Series(fcl)
print(scw)
print(fcl["from_this_person_to_poi"])

# What’s the value of stock options exercised by Jeffrey K Skilling?
fskj = enron_data["SKILLING JEFFREY K"]
sskj = pd.Series(fskj)
print(sskj)
print(fskj["exercised_stock_options"])

# Of these three individuals (Lay, Skilling and Fastow), who took home the most money (largest value of “total_payments” feature)?
flk = enron_data["LAY KENNETH L"]
slk = pd.Series(flk)
print(slk)

ffa = enron_data["FASTOW ANDREW S"]
sfa = pd.Series(ffa)
print(sfa)

print(fskj["total_payments"])
print(flk["total_payments"])
print(ffa["total_payments"])