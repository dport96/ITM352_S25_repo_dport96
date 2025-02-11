"""
Define a list of survey response values (5, 7, 3, and 8) and store them in
a variable. Next define a tuple of respondent ID values 
(1012, 1035, 1021, and 1053). Use the .append() method to append the tuple
to the list. Print out the list. 
"""

survey_responses = [5, 7, 3, 8]
respondent_IDs = (1012, 1035, 1021, 1053)

a = [(1012,5),(1035,7)] # better way to store idd and responses

survey_responses.append(respondent_IDs)

print(survey_responses)