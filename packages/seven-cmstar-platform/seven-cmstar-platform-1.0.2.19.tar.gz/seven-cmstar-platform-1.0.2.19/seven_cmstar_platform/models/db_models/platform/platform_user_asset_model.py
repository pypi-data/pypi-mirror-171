
#此文件由rigger自动生成
from seven_framework.mysql import MySQLHelper
from seven_framework.base_model import *


class PlatformUserAssetModel(BaseModel):
    def __init__(self, db_connect_key='db_platform', sub_table=None, db_transaction=None, context=None):
        super(PlatformUserAssetModel, self).__init__(PlatformUserAsset, sub_table)
        self.db = MySQLHelper(config.get_value(db_connect_key))
        self.db_connect_key = db_connect_key
        self.db_transaction = db_transaction
        self.db.context = context

    #方法扩展请继承此类
    
class PlatformUserAsset:

    def __init__(self):
        super(PlatformUserAsset, self).__init__()
        self.id = 0  # id
        self.id_md5 = 0  # id_md5(act_id+user_id+asset_type+asset_object_id)md5int生成
        self.app_id = ""  # 应用标识
        self.act_id = 0  # 活动标识
        self.user_id = 0  # 用户标识
        self.open_id = ""  # open_id
        self.user_nick = ""  # 用户昵称
        self.asset_type = 0  # 资产类型(1-次数2-积分3-价格档位，业务自定义类型从101起，避免跟公共冲突)
        self.asset_object_id = ""  # 资产对象标识
        self.asset_value = 0  # 资产值
        self.asset_check_code = ""  # 资产检验码(id+asset_value+加密签名)md5生成
        self.create_date = "1900-01-01 00:00:00"  # 创建时间
        self.modify_date = "1900-01-01 00:00:00"  # 修改时间

    @classmethod
    def get_field_list(self):
        return ['id', 'id_md5', 'app_id', 'act_id', 'user_id', 'open_id', 'user_nick', 'asset_type', 'asset_object_id', 'asset_value', 'asset_check_code', 'create_date', 'modify_date']
        
    @classmethod
    def get_primary_key(self):
        return "id"

    def __str__(self):
        return "platform_user_asset_tb"
    