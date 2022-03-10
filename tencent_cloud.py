
from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
from qcloud_cos import CosServiceError
from qcloud_cos import CosClientError

secret_id = 'xxxxxxxxxxxxxxxxxxxx'     # 替换为用户的secret_id
secret_key = 'xxxxxxxxxxxxxxxxxxx'     # 替换为用户的secret_key
region = 'ap-shanghai'    # 替换为用户的region
token = None               # 使用临时密钥需要传入Token，默认为空,可不填
config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key, Token=token)  # 获取配置对象
client = CosS3Client(config)
def up_tencent(localfilepath,key):
    client.upload_file(
        Bucket='huang-1258465420',
        LocalFilePath=localfilepath,#'D:\图片/v2-6cd79620efc0e75e5aed53df917addbd_r.jpg',
        Key=key,#'web_file/picture.jpg',
        PartSize=1,
        MAXThread=10,
        EnableMD5=False
)

