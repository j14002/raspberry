# -*-  coding: utf-8 -*-
import MySQLdb
import json
import collections


if __name__ == "__main__":
	connector = MySQLdb.connect(host="localhost", db="j14002", user="root",passwd="teikyo",charset="utf8")
	cursor = connector.cursor()
	f = open('data.json','r')
        jsonData = json.load(f,object_pairs_hook = collections.OrderedDict)


        for num in jsonData:
	    sql = "insert into user(hikari) values(" + str(jsonData[num]) + ")"
	    cursor.execute(sql)
	
	connector.commit()
	cursor.close()
	connector.close()










