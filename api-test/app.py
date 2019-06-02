'''
au:l
di:flask RESTFUL api
'''
from flask import Flask, make_response, jsonify, request

from .database import db_session
from .database import init_db

from flask_cors import *

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app, supports_credentials=True)

# return a session
from .models import trans


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


"""
__tablename__ = 'bigdata


API sqlalchemy 
"""


@app.route("/api/data/query_col/<col>/",methods=['GET'])
def get_col(col):
    """

    :param col:  查询的列名字
    :return:
    """
    col_list = ["number", "jobType", "jobName", "city",
                "companyName", "company_size", "company_type",
                "eduLevel", "recruit", "salary"]
    if col in col_list:

        sql_str = "select count(%s),%s from bigdata group by %s" % (col, col, col)
    else:
        return jsonify({
            "status":"fail",
            "data":"not the column name:%s" % col
        })
    res = db_session.execute(sql_str).fetchall()

    new_res = []
    for idx in range(len(res)):
        temp_res = {
            "数量": res[idx][0],
            col: res[idx][1]
        }
        new_res.append(temp_res)
    print(new_res)

    if col in col_list:
        return jsonify({
            "data": list(new_res),
            "status": "success"
        })
    else:
        return jsonify({
            "data":"not found",
            "status":"fail"
        })


@app.route('/api/bigdata/query_jobType/<col_id>/', methods=['GET'])
def get_jobtype(col_id):
    """
    查询数据库 中 jobType 的数目
    在 url 中 以 jobType 的中文查询
    返回整理后的 {}

    :param col_id:
    :return:
    """

    sql_str = "SELECT COUNT(jobType), jobType FROM bigdata GROUP BY jobType"

    res = db_session.execute(sql_str).fetchall()

    print("====")
    print(res[0][0])
    print(res[0][1])
    print("====")
    # --> [{id:id,col:value}]

    new_res = []

    for idx in range(len(res)):
        temp_res = {
            "number": res[idx][0],
            "name": res[idx][1]
        }
        new_res.append(temp_res)
    # res = json.dumps(new_res,ensure_ascii=False)

    res_item = filter(lambda x: x["name"] == col_id, new_res)
    res_item = list(res_item)
    if col_id == "all":
        return jsonify({
            "status": 200,
            # "data": list(new_res)
            "data": new_res
        })

    if len(res_item) == 0:
        return jsonify({"status": "false",
                        "data": "no such jobType"})
    else:
        # return json.dumps(res_item, ensure_ascii=False)
        return jsonify({
            "status": 200,
            "data": list(new_res)

        })


@app.route('/api/bigdata/query_jobName/<clo_name>/', methods=['GET'])
def get_jobname(clo_name):
    sql_str = "select jobName,count(jobName) from bigdata group by jobName"

    res = db_session.execute(sql_str).fetchall()
    # res = json.dumps(res,ensure_ascii=False)
    print("====")
    print(res[0][0])
    print(res[0][1])
    print("====")
    new_res = []
    for idx in range(len(res)):
        name = str(res[idx][0]).replace(" ", "")
        temp_res = {
            "jobName": name,
            "数量": res[idx][1]
        }
        new_res.append(temp_res)
    item = filter(lambda x: x['jobName'] == clo_name, new_res)
    item = list(item)
    new_res = list(new_res)

    # return json.dumps(new_res,ensure_ascii=False),200,{'Content-Type': 'application/json'}
    if clo_name == "all":
        return jsonify({
            "status": "success",
            "data": new_res
        })
    if len(item) == 0:
        return jsonify({
            "status": "why are u so waste",
            "data": "no such jobName"
        })

    else:
        return jsonify({
            "status": "success",
            "data": jsonify(item, ensure_ascii=False)
        })


"""
api
"""


@app.route("/api/countName")
def count_name():
    """
    执行 sql 查询

    :return:  a json data
    """
    init_db()
    print('/api/countName"')
    res = db_session.query(trans.transCSV).all()
    # res --->[<class>,<class>...<class>]
    res = trans_data(res)
    # res = json.dumps(res)
    return ""


# ss = Mysql.set_sql_str("ss")


# db.session.execute(sql)


"""
function
"""


# write header
def set_header_for_data(data):
    '''

    :param data:    can models to Json
    :return:
    '''

    print(data)


def trans_data(data):
    '''

    :param data:   session 执行原生sql 查询到的class
                    是一个  [{key:value,key:vlaue},{}...{}]
    :return:  [{},{}...{}] 整理后的数据
    '''

    """
    每一种数据的格式不一样  所以这是一个对 trans 类型 做的处理
    
    vars(data[0]): 
    
    {'_sa_instance_state': <sqlalchemy.orm.state.InstanceState object at 0x00000207A1A206A0>,
     'LAST_FLIGHT_DATE': datetime.datetime(1999, 4, 16, 16, 16, 37), 
     'SUM_YR_1': 17678, 'FLIGHT_COUNT': 21, 'avg_discount': 0.083, 'SUM_YR_2': 16994, 
     'LOAD_TIME': datetime.datetime(2019, 5, 26, 11, 12, 16), 
     'name': 'Sandra Gonzalez', 
     'FFP_DATE': datetime.datetime(2002, 8, 14, 18, 8, 53)}

     
     <class 'sqlalchemy.orm.state.InstanceState'>
     <class 'float'>
     <class 'int'>
     <class 'int'>
     <class 'datetime.datetime'>
     <class 'str'>
     <class 'datetime.datetime'>
     <class 'datetime.datetime'>
     <class 'int'>
     
    """

    for idx in range(len(data)):
        temp = vars(data[idx])
        for key in temp:
            # print(type(temp[key]))
            value = temp[key]
            value_type = type(temp[key])
            if (value_type == 'sqlalchemy.orm.state.InstanceState'):
                print(1)

                pass

    return []
