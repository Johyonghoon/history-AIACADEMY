import pymysql
from app.configs.chatbot.database import *  # DB 접속 정보 불러오기

db = None
try:
    db = pymysql.connect(
        host=HOSTNAME,
        user=USERNAME,
        passwd=PASSWORD,
        db=DATABASE,
        charset=CHARSET
    )

    # 테이블 생성 sql 정의
    sql = '''
      CREATE TABLE IF NOT EXISTS `chatbot_train_data` (
      `id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
      `intent` VARCHAR(45) NULL,
      `ner` VARCHAR(1024) NULL,
      `query` TEXT NULL,
      `answer` TEXT NOT NULL,
      `answer_image` VARCHAR(2048) NULL,
      PRIMARY KEY (`id`))
    ENGINE = InnoDB DEFAULT CHARSET=utf8mb4
    '''

    # 테이블 생성
    with db.cursor() as cursor:
        cursor.execute(sql)

except Exception as e:
    print(e)

finally:
    if db is not None:
        db.close()

