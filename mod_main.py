from mod_fileExtract import FileExtract
from mod_jsonExtract import JsonExtract
from mod_sqlExtract import SqlExtract
from mod_sqlImport import SqlImport

if __name__ == '__main__':
    def main():
        obj_sqlDestination = SqlImport('10.19.17.12','root','password','dbEtl')

        #Create destination table
        obj_sqlDestination.open()
        obj_sqlDestination.recreateTableDestination()

        obj_file = FileExtract("sources/week_cust.csv", obj_sqlDestination)
        obj_json = JsonExtract("sources/cust_data.json", obj_sqlDestination)
        obj_sql = SqlExtract('10.19.17.12','root','password','dbClient', obj_sqlDestination)

        objList = [obj_file,obj_json,obj_sql]
        for obj in objList:
            obj.open()
            obj.readAndExtract()
            obj.close()

            obj_sqlDestination.close()


main()