from flask import Flask, render_template, jsonify
app = Flask(__name__)

Projects =[
  {"id":1,
  "Title":"Webscraping TMDB",
   "Summary":" ",  "Link":"https://colab.research.google.com/drive/1O4AU7aLXRKzinKcT1k3VP6lty-0Rqtnt?usp=sharing"},
  
  {"id":2,
  "Title":"Medical Retinopathy Image Classification-Pytorch",
   "Summary":" ",
  "Link":" "},
  
  {"id":3,
  "Title":"Air-Quality India EDA",
   "Summary":" ",
  "Link":" "},
  
  {"id":4,
  "Title":"Elo Customer Segmentation using XGBoost",
   "Summary":" ",
  "Link":" "}  
]

Certificates =[
  {"id":1,
  "Title":"DataScience and Machine Learning Bootcamp",
  "Link":" "},
  
  {"id":2,
  "Title":"Machine Learning with Python",
  "Link":" "},
  
  {"id":3,
  "Title":"Deep Learning with Pytorch",
  "Link":" "}
]

@app.route("/")
def html_webpage():
  return render_template('home.html', projects=Projects, certificates =Certificates)

@app.route("/api/projects")
def load_projects():
  return jsonify(Projects+Certificates)

if __name__=="__main__":
  app.run(host="0.0.0.0", debug = True)