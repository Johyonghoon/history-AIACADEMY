from sqlalchemy import Column, TIMESTAMP as Timestamp, text
from datetime import datetime, timedelta


class TimestampMixin(object):
    kst = datetime.utcnow() + timedelta(hours=9) # 한국 표준시인 KST는 UTC로부터 9시간을 더하면 된다
    now = kst.strftime("%Y-%m-%d %H:%M:%S")
    created_at = Column(Timestamp, nullable=False, server_default=text('current_timestamp'))
    updated_at = Column(Timestamp, nullable=False, server_default=text('current_timestamp on update current_timestamp'))