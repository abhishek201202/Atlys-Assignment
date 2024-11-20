import os
import csv
import json

class scrapper_dml: 
    async def insert(data, transaction_id = 'default'):
        try:
            file_path =  os.getcwd()+'/scrapper/dm/store.json'
            with open(file_path, "a") as json_file:
                json.dump(data, json_file, indent=4)
            print('Data saved successfully')
        except Exception as e:
            print(f"An error occurred while writing to the file: {e}")

    async def get():
        file_path =  os.getcwd()+'/scrapper/dm/store.json'
        data = []
        with open(file_path, "r") as json_file:
            data = json.load(json_file)
        return data
