import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')

def get_signal(ts_code, table="signal"):
    """
    获取 codeen
    :param fut_code:"AP"
    :param exchange:"CZCE"
    :param table:
    :return:
    """

    table = dynamodb.Table(table)
    try:
        response = table.get_item(Key={'ts_code': ts_code})
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print(response)
        if "Item" in response:
            return response['Item']
        else:
            return None

def get_fut_code(fut_code, table="fut_code"):
    """
    获取 codeen
    :param fut_code:"AP"
    :param exchange:"CZCE"
    :param table:
    :return:
    """

    table = dynamodb.Table(table)
    try:
        print(fut_code)
        print(table.get_item(Key={'fut_code': fut_code}))
        print(fut_code)
        response = table.get_item(Key={'fut_code': fut_code})
        print(response)
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print(response)
        if "Item" in response:
            return response['Item']
        else:
            return None
