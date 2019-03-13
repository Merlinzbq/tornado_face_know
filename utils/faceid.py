
from aip import AipFace

APP_ID = '15750965'
API_KEY = 'R8vFwISg2pARS8SjFtPKZElB'
SECRET_KEY = 'kd3amWfp3Ywap02Fx3PElwKI2Fhmxdwn'

client = AipFace(APP_ID, API_KEY, SECRET_KEY)


def face_register(image, userId, imageType='BASE64', groupId='test'):
    """ 调用人脸注册 """
    res = client.addUser(image, imageType, groupId, userId)
    print(res)
    # 响应内容错误的json数据: {'error_code': 222202, 'error_msg': 'pic not has face', 'log_id': 1368654424876672171, 'timestamp': 1552487667, 'cached': 0, 'result': None}
    # 响应正确的json数据: {'error_code': 0, 'error_msg': 'SUCCESS', 'log_id': 1345050724876733281, 'timestamp': 1552487673, 'cached': 0, 'result': {'face_token': 'b710bf1182ce01078f136a6b2704d58d', 'location': {'left': 36.44, 'top': 71.45, 'width': 25, 'height': 29, 'rotation': -1}}}
    if res['error_code']:
        return False
    return True


def face_valid(image, imageType='BASE64'):
    """校验人脸"""
    # 校验结果返回的json数据同人脸注册
    res = client.detect(image, imageType)
    if res['error_code']:
        return False
    return True

