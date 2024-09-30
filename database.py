from sqlalchemy import *
engine = create_engine("mysql+pymysql://root:password@localhost/flask?charset=utf8mb4",
    # connect_args={
    #         "ssl": {
    #             "ca": "/home/gord/client-ssl/ca.pem",
    #             "cert": "/home/gord/client-ssl/client-cert.pem",
    #             "key": "/home/gord/client-ssl/client-key.pem"
    #         }
    #     }include if planet scale is used
    )

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text('select * from jobs'))
    jobs = []
    for row in result.all():
      jobs.append(row._asdict())
    return jobs


def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text('select * from jobs where id = :val').bindparams(val=id))
    rows = result.fetchone()
    if rows:
      return rows
    else:
      return None

def store_app_data(job_id,data):
  with engine.connect() as conn:
    query = text('insert into application (job_id, full_name,email,linkedin_url,education,work_exp,resume_uel) values (:jobid,:fullname,:email,:linkedin,:edu,:workex,:resume)')
    params = {
      'jobid':job_id,
      'fullname': data['full_name'],
      'email' : data['email'],
      'linkedin' : data['linkedin'],
      'edu' : data['education'],
      'workex' : data['workexp'],
      'resume' : data['resume']
    }
    conn.execute(query,params)
    conn.commit()

  
# with engine.connect() as conn:
#     result = conn.execute(text('select * from jobs'))
#     # print(type(result)) #cursor
#     # result_all = result.all()
#     # print(type(result_all)) #list
#     # first_result = result_all[0]
#     # print(type(first_result))# <class 'sqlalchemy.engine.row.Row'>
#     # first_result_dict = result_all[0]._asdict()
#     # print(type(first_result_dict))
#     # print(first_result_dict)
#     result_dict = []
#     for row in result.all():
#         result_dict.append(row._asdict())
    
#     print(result_dict)


