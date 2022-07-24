import pymysql.cursors

conn = pymysql.connect(host = '10.10.20.40', 
                            user='admin', 
                            password ='1234', 
                            db='attendance', 
                            charset='utf8mb4', 
                            cursorclass=pymysql.cursors.DictCursor)

try:
    c =  conn.cursor()
    c.execute("SELECT * FROM user")    
    #print(c.fetchall())

    
    rows = c.fetchall()    
    for i in rows:
        print(i)
        
finally:
    c.close()
    conn.close()    
