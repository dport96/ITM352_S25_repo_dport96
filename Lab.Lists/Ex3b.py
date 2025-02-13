survey_responses = [5, 7, 3, 8]
survey_responses = survey_responses + [0]
survey_responses = survey_responses[:2] + [6] + survey_responses[2:]
print(survey_responses)