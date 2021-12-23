import pymysql
import sys
import pandas as pd
from util.config import sql_config
from sqlalchemy import create_engine


def err_exit():
    print("error")
    sys.exit(0)


def suc_exit():
    print("success")
    sys.exit(0)


# 用于导入数据库
if __name__ == "__main__":
    if len(sys.argv) <= 1:
        err_exit()
    file = sys.argv[1]
    if not file.endswith(".csv"):
        err_exit()
    name = file.split('.')[0]
    print(name)
    df = pd.read_csv(file)
    engine = create_engine(sql_config)
    df.to_sql(name, con=engine, if_exists='replace', index=False)
    suc_exit()
