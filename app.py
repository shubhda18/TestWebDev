from flask import Flask, render_template
app = Flask(__name__)

Projects =[
  {"id":1,
  "Title":"Webscraping TMDB",
  "Link":" "},
  {"id":2,
  "Title":"Medical Retinopathy Image Classification-Pytorch",
  "Link":" "},
  {"id":3,
  "Title":"Air-Quality India EDA",
  "Link":" "},
  {"id":1,
  "Title":"Elo Customer Segmentation using XGBoost",
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
  return render_template('home.html', projects="Projects", certificates ="Certificates")
  print(__name__)

if __name__=="__main__":
  app.run(host="0.0.0.0", debug = True)