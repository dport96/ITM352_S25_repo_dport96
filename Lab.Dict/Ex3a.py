survey_responses = [5, 7, 3, 8]
respondent_IDs = (1012, 1035, 1021, 1053)

responses = dict(zip(respondent_IDs,survey_responses))
responses[1234] = 10
print(responses)