from mod_fileExtract import FileExtract
from mod_jsonExtract import JsonExtract

if __name__ == '__main__':
    def main():
        #
        obj_file = FileExtract("sources/week_cust.csv")
        obj_json = JsonExtract("sources/cust_data.json")
        objList = [obj_file,obj_json]
        for obj in objList:
            obj.open()
            obj.readSource()

main()