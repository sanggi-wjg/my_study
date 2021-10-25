## Pipeline 작성
### Python package
Python으로 Pipeline 작성하자
```shell script
pip install virtualenv
# 1.4 이상은 에러 발생
pip install SQLAlchemy==1.3.23 
pip install apache-airflow
pip install apache-airflow['cncf.kubernetes']
```

### Before Testing
```shell script
# check ~/airflow/airflow.cfg

# dags default 경로 
# dags_folder = /root/airflow/dags 
```

### Testing
```shell script
python3 ~/airflow/dags/sample.py
# If the script does not raise an exception 
# it means that you have not done anything horribly wrong, 
# and that your Airflow environment is somewhat sound.
```

### Airflow metadata validation
```shell script
# initialize the database tables
airflow db init

# DB: sqlite:////root/airflow/airflow.db
# [2021-10-25 08:18:50,515] {db.py:823} INFO - Creating tables
# INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
# INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
# WARNI [airflow.models.crypto] empty cryptography key - values will not be stored encrypted.
# Initialization done

# print the list of active DAGs
airflow dags list

# dag_id                                  | filepath                                                                                               | owner   | paused
# ========================================+===============================================================+=========+=======
# SampleDAG                               | sample.py                                                     | WMS     | True 

# prints the list of tasks in the "tutorial" DAG
airflow tasks list SampleDAG

# prints the hierarchy of tasks in the "tutorial" DAG
airflow tasks list SampleDAG --tree

# airflow tasks  test [dag_id] [task_id] [logical_date]
airflow tasks test SampleDAG bash_print_date 2015-06-01
airflow tasks test SampleDAG bash_sleep 2015-06-01
airflow tasks test SampleDAG bash_template 2015-06-01

# airflow dags test [dag_id] [logical_date]
# While it does take task dependencies into account, no state is registered in the database. 
# It is convenient for locally testing a full run of your DAG, given that e.g. 
# if one of your tasks expects data at some location, it is available
airflow dags test SampleDAG 2015-06-01
```

## Backfill
```shell script
airflow dags backfill tutorial --start-date 2021-10-24
# optionally --end-date 2021-10-31
```