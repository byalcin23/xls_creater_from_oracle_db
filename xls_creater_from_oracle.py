import cx_Oracle
import os
import pandas as pd

conn_str = u'USER_NAME/PASSWORD@DOMAIN_OR_IP_ADDRESS:PORT/SERVICE_NAME'
conn = cx_Oracle.connect(conn_str)
c = conn.cursor()

sql_query1 = """
SQL QUERY HERE
"""



#------------İLKSQL---------------
c.execute(u"{0}".format(sql_query1))
get1 = c.fetchall()
columns1 = [description[0] for description in c.description]
df = pd.DataFrame(get1, columns=columns1)
df.to_excel('NAME_OF_DOC.xlsx', index=False, engine='openpyxl')
#------------İLKSQL---------------




# Dosya yolları
file_path1 = os.path.join(os.getcwd(), 'NAME_OF_DOC.xlsx')


# E-posta gönderme komutu
os.system('echo "MAIL BODY" | mailx -s "SUBJECT OF EMAIL" -r "SENDER@EMAIL.COM" -a "{0}" -a "{1}" RECIEPENT1@byalcin23.com RECIEPENT2@byalcin23.com                                                                                                                            @vodafone.com ali.demirbas@vodafone.com yeliz.bayrak@vodafone.com'.format(file_path1, file_path2))
