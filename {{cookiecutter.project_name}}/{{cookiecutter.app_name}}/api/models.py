#  api 数据库结构模型

from datetime import datetime

from {{cookiecutter.app_name}}.database import Column, Model, SurrogatePK, db


class Demo(SurrogatePK, Model):
    """
    用户表
    """
    __tablename__ = "demo"
    field_1 = Column(db.String(512), nullable=False, unique=True, comment="字段1")
    field_2 = Column(db.String(512), nullable=False, unique=True, comment="字段2")
    active = Column(db.Boolean(), default=False, nullable=False, comment="是否有效")
    created = Column(db.DateTime, nullable=False, default=datetime.now, comment="创建时间")
    updated = Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now, comment="更新时间")

    # 状态枚举
    ERROR = -1
    WAIT_RUN = 0
    RUNNING = 1
    SUCCEED = 2
    FAIL = 3

    # 默认倒序
    __mapper_args__ = {"order_by": created.desc()}

    def __repr__(self):
        return str(f"user_id={self.user_id} user_name={self.user_name}")