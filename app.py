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
            6: 'I have hands on experience on Deep Neural Networks (DNN) & transforming data science prototypes to production-grade solutions. ',
            7: 'I have hands on experience on Convolutionary Neural Networks (CNN). ',
            8: 'I have knowlege in NLP using LSTM. ',
            9: 'I have knowledge of deploying ML models using cloud technologies. ',
            10: 'I am self-motivated, a self-starter and have a creative & problem solving mentality. '}

    keywords = {'requirement': 3, 'Python': 4, 'Machine': 5, 'Deep': 6, 'Image': 7, 'language': 8, 'opensource': 1, 'positive': 2, 'switch': 2, 'solutions': 3, 'python': 4, 'machine': 5, 'DNN': 6, 'CNN': 7, 'NLP': 8, 'cloud': 9, 'self':10, 'solving': 10, 'creative': 10}
    matching_skills = []
    with open("company_requirement.txt") as openfile:
        for line in openfile:
            for part in line.split():
                for key in list(keywords.keys()):
                    if key in part:
                        matching_skills.append(keywords[key])
    matching_skills = list(dict.fromkeys(matching_skills))
    print(matching_skills)
    match = ''
    for i in matching_skills:
        match = match + '\n' + my_skills[i]


    if request.method == 'POST':
        
        Company_Name=request.form['Company_Name']
        
        return render_template('index.html',prediction_text="{}".format(match))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)

