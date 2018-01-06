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
import math

enron_data = pickle.load(open("final_project/final_project_dataset.pkl", "r"))

# How many data points (people) are in the dataset?
print("1 -> " + str(len(enron_data.keys())))

# For each data point (person) how many features are available?
print("2 -> " + str(len(enron_data.values()[0].keys())))

# How many POIs are in the dataset?
# data[person_name]["poi"]==1
print("3 -> " + str(len(list(v for v in enron_data.values() if v["poi"] == 1))))

# What is the total value of the stock belonging to James Prentice?
print("4 - PRENTICE JAMES total_stock_value -> " + str(enron_data["PRENTICE JAMES"]["total_stock_value"]))

# How many email messages do we have from Wesley Colwell to persons of interest?
print("5 - COLWELL WESLEY from_this_person_to_poi -> " + str(enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]))

# What’s the value of stock options exercised by Jeffrey K Skilling?
print("6 - SKILLING JEFFREY K exercised_stock_options -> " + str(enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]))

# Of these three individuals (Lay, Skilling and Fastow), who took home the most money (largest value of “total_payments” feature)?
print("7 - SKILLING JEFFREY K total_payments -> " + str(enron_data["SKILLING JEFFREY K"]["total_payments"]))
print("7 - LAY KENNETH L total_payments -> " + str(enron_data["LAY KENNETH L"]["total_payments"]))
print("7 - FASTOW ANDREW S total_payments -> " + str(enron_data["FASTOW ANDREW S"]["total_payments"]))

# How many folks in this dataset have a quantified salary? Known email address?
print("8 -> " + str(len(list(v for v in enron_data.values() if math.isnan(float(v["salary"])) == 0))))
print("8 -> " + str(len(list(v for v in enron_data.values() if v["email_address"] != "NaN"))))