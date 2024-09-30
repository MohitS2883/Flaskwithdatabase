from flask import *
from database import engine, load_jobs_from_db,load_job_from_db,store_app_data
from sqlalchemy import text
import datetime
app = Flask(__name__)
# JOBS = [
#   {
#     'id':1,
#     'title':'Data Analyst',
#     'location':'Bengaluru ,India',
#     'salary': 'Rs.10,00,000'
#   },
#   {
#     'id':2,
#     'title':'Data Scientist',
#     'location':'Delhi ,India',
#     'salary': 'Rs.15,00,000'
#   },
#   {
#     'id':3,
#     'title':'Frontend Engineer',
#     'location':'Remote',
#     'salary': 'Rs.10,00,000'
#   },
#   {
#     'id':4,
#     'title':'Backend Engineer',
#     'location':'San Fransisco ,USA',
#     'salary': '$.10,00,000'
#   }
# ]

    


@app.route("/")
def hello():
  jobs = load_jobs_from_db()
  return render_template("home.html",job=jobs,company="Mohit")

@app.route("/api/jobs")
def list_jobs():
  jobs = load_jobs_from_db()
  return jsonify(jobs)

@app.route("/job/<id>")
def show_job(id):
  job = load_job_from_db(id)
  if not job:
    return "Not Found", 404
  return render_template('jobpage.html',job=job)

@app.route('/job/<id>/apply',methods=['post'])
def apply_to_job(id):
  # data = request.args used when no method is used
  d = datetime.datetime.now()
  job = load_job_from_db(id)
  data = request.form
  store_app_data(id,data)
  return render_template('appl.html',application=data,job=job,date=d)



if __name__ == "__main__":
  app.run(host="0.0.0.0",debug=True)