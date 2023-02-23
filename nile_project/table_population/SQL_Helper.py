import sqlite3
import os

class mysqlite3():
    db_path = './nile_project/table_population/file.db'
    def __init__(self): 
        if os.path.isfile(self.db_path):
            os.remove(self.db_path)
            print('\nFile already exists. Reinitializing database.\n')
        else:
            print('\nCreating database\n')
        self.connection = sqlite3.connect(self.db_path)
        self.cur = self.connection.cursor()

    def __enter__(self): 
        return self

    def __exit__(self, ext_type, exc_value, traceback):
        self.cur.close()
        if isinstance(exc_value, Exception):
            self.connection.rollback()
        else:
            self.connection.commit()
        self.connection.close()

    def create_table(self, fields):
        columns = "(" + ",\n".join(["{} {}".format(k,v) for k,v in fields['Trip_info'].items()]) + ")"
        self.cur.execute("CREATE TABLE Trip_info\n" + columns)

    def executemany(self, data):
        self.cur.executemany("INSERT INTO Trip_info VALUES (?, ?, ?, ?, ?)", self.dict_to_list_for_import(data))

    def dict_to_list_for_import(self, some_dict: dict) -> list:
        lst = []
        for tple in some_dict.items():
            outerlst = []   
            for item in tple:
                if type(item) == tuple:
                    for i in item:
                        outerlst.append(i)
                else:
                    outerlst.append(item)
            lst.append(outerlst)
        return lst

