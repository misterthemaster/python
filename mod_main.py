from mod_fileExtract import FileExtract
from mod_jsonExtract import JsonExtract
from mod_sqlExtract import SqlExtract

if __name__ == '__main__':
    def main():
        #
        obj_file = FileExtract("sources/week_cust.csv")
        obj_json = JsonExtract("sources/cust_data.json")
        obj_sql = SqlExtract('10.19.17.12',
                             'root',
                             'password',
                             'dbClient')

        objList = [obj_file,obj_json,obj_sql]
        for obj in objList:
            obj.open()
            obj.readAndExtract()
            obj.close()

main()