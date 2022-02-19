from flask import Flask, render_template, request
import jsonify
import requests
import numpy as np
app = Flask(__name__)
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


@app.route("/predict", methods=['POST'])



def predict():
    my_skills = {1: 'I have good knowledge of working in and developing programs using open source languages and tools. ',
            2: 'I have a positive "Lets do it!" attitude. ',
            3: 'I am excellent at understanding the core business model, analyzing company reports, identifying problems & critical areas, and providing best solutions for the company to get an edge over its competition. ',
            4: 'I have hands on experience with Python and its various Libraries. ',
            5: 'I have hands on experience on various Machine Learning (ML) Algorithms and skilled in extracting valuable information from data. ',
            6: 'I have hands on experience on SAP Basis and monitoring activities. ',
            7: 'I have hands on experience on various upgrades viz. Kernel, DB2, Hana Patching, DB2 Fix Pack, C-CEE Upgrade, ST/PI, ST-A/PI etc. ',
            8: 'I am a team player who can assist and guide team members whenever possible. ',
            9: 'I have automated Basis tasks like monitoring, job ticket creation, dumps analysis etc ',
            10: 'I have hands on experience on various Automation and RPA technologies viz. Python, pyautogui, Automation Anywhere, UI Path, Splunk '}

    keywords = {'Requirements': 3, 'Python': 4, 'Machine': 5, 'Basis': 6, 'Kernel': 7, 'team': 8, 'python': 10, 'positive': 2, 'switch': 2, 'solutions': 3, 'python': 4, 'machine': 5, 'basis': 9, 'automation': 10, '(RPA)': 10, 'administration': 9, 'Automation':10, 'RPA': 10, 'creative': 10}
    matching_skills = []
    with open("company_requirement.txt") as openfile:
        for line in openfile:
            for part in line.split():
                for key in list(keywords.keys()):
                    if key in part:
                        matching_skills.append(keywords[key])
    matching_skills = list(dict.fromkeys(matching_skills))
    print(matching_skills)
    common_skills = ['7','9','10']
    for i in common_skills:
        matching_skills.append(i)
    match = ''
    for i in matching_skills:
        match = match + '\n' + my_skills[i]


    if request.method == 'POST':
        
        
        return render_template('index.html',prediction_text="{}".format(match))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)

