from datetime import timedelta, datetime
from textwrap import dedent

from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner'           : 'WMS',
    'depends_on_past' : False,
    'email'           : ['jay_g@kr.accommate.com'],
    'email_on_failure': True,
    'email_on_retry'  : False,
    'retires'         : 3,
    'retry_delay'     : timedelta(minutes = 2),

}

with DAG(
    dag_id = 'SampleDAG',
    default_args = default_args,
    description = 'Sample DAG',
    schedule_interval = timedelta(minutes = 5),
    start_date = datetime(2021, 10, 22),
    catchup = False,
    tags = ['Sample'],
) as dag:
    task1 = BashOperator(
        task_id = 'bash_list_human',
        bash_command = 'ls -h'
    )
    task2 = BashOperator(
        task_id = 'bash_disk_human',
        depends_on_past = False,
        bash_command = 'df -h',
        retries = 3
    )

    task1.doc_md = dedent(
        """
        ### This Is Docs!
        Hello World
        ![img](http://montcs.bloomu.edu/~bobmon/Semesters/2012-01/491/import%20soul.png)
        """
    )
    dag.doc_md = __doc__
    dag.doc_md = "documentation placed"
    templated_command = dedent(
        """
        {% for i in range(5) %}
            echo "{{ ds }}"
            echo "{{ macros.ds_add(ds, 7)}}"
            echo "{{ params.foo }}"
        {% endfor %}
        """
    )

    task3 = BashOperator(
        task_id = 'bash_template',
        depends_on_past = False,
        bash_command = templated_command,
        params = { 'foo': 'var' },
    )

    task1 >> [task2, task3]
