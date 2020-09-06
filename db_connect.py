import pymysql
 
### MySQL Connection 연결
conn = pymysql.connect(host='auroralab-mysql-cluster', 
                        user='masteruser', password='xxxx',
                        db='employees', charset='utf8')
 
# Connection 으로부터 Cursor 생성
curs = conn.cursor()
 
# SQL문 실행
sql = "select * from employees limit 10"
curs.execute(sql)
 
# 데이타 Fetch
rows = curs.fetchall()
print(rows)     # 전체 rows
 
# Connection 닫기
conn.close()