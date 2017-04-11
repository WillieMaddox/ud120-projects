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

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

for person, attributes in enron_data.iteritems():
    if attributes["poi"] == 1:
        print person

i = 0
for person, attributes in enron_data.iteritems():
    if attributes["email_address"] != 'NaN':
        i += 1
print i

i = 0
for person, attributes in enron_data.iteritems():
    if attributes["salary"] != 'NaN':
        i += 1
print i

print len(enron_data)
