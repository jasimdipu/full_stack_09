import mysql.connector as conn


class DBHelper:

    def __init__(self) -> None:
        pass

    def __db_connection(self, host="localhost", username='root', password='', db_name=""):

        try:
            db = conn.connect(host=host, username=username,
                              password=password, database=db_name)
            print(db)
            return db
        except Exception as e:
            print(e)

    def create_database(self, database=""):
        try:
            db = self.__db_connection()
            query = "CREATE DATABASE "+database
            cursor = db.cursor()
            cursor.execute(query)

            cursor.close()
            db.close()

        except Exception as e:
            print(e)

    def create_table(self, db_name, table_name):
        try:
            db = self.__db_connection(db_name=db_name)
            query = "CREATE TABLE {}(id integer primary key auto_increment, name varchar(255), dept varchar(255))".format(
                table_name)
            cursor = db.cursor()
            cursor.execute(query)
            db.commit()
            print("table {} is created".format(table_name))
            cursor.close()
            db.close()

        except Exception as e:
            print(e)

    def insert_val(self, db_name, table_name, id, name, dept):
        try:
            db = self.__db_connection(db_name=db_name)
            query = "INSERT INTO {}(id, name, dept) VALUES(%s, %s, %s)".format(
                table_name)
            value = (id, name, dept)
            cursor = db.cursor()
            cursor.execute(query, value)
            db.commit()
            print("Value inserted")
            cursor.close()
            db.close()

        except Exception as e:
            print(e)

    def fetch_data(self, db_name, table_name):
        try:
            db = self.__db_connection(db_name=db_name)
            query = "SELECT * FROM "+table_name
            cursor = db.cursor()
            cursor.execute(query)
            res = cursor.fetchall()
            for i in res:
                print(res)
            cursor.close()
            db.close()

        except Exception as e:
            print(e)

    def fetch_single_data(self, db_name, table_name, id):
        try:
            db = self.__db_connection(db_name=db_name)
            query = "SELECT * FROM {} WHERE id={}".format(table_name, id)
            cursor = db.cursor()
            cursor.execute(query)
            res = cursor.fetchall()
            for i in res:
                print(res)
            cursor.close()
            db.close()

        except Exception as e:
            print(e)

    def delete_val(self, db_name, table_name, id):
        try:
            db = self.__db_connection(db_name=db_name)
            query = "DELETE FROM {} WHERE id={}".format(table_name, id)
            cursor = db.cursor()
            cursor.execute(query)
            db.commit()
            print("Value DELETED")
            cursor.close()
            db.close()

        except Exception as e:
            print(e)


db_op = DBHelper()

# db_op.create_database('student')
# db_op.create_table("student", "stu_info")


# db_op.insert_val("student", "stu_info", 0, "tamim", "CSE")
# db_op.insert_val("student", "stu_info", 1, "faruqe", "IT")
# db_op.insert_val("student", "stu_info", 2, "Hasan", "BBA")
# db_op.insert_val("student", "stu_info", 3, "abdullah", "MBA")

# db_op.fetch_data("student", "stu_info")

# db_op.delete_val("student", "stu_info", 1)
db_op.fetch_single_data("student", "stu_info", 2)
