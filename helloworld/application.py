#!flask/bin/python
import json
from decimal import Decimal

import boto3
from boto3.dynamodb.conditions import Key
from flask import Flask, Response
from helloworld.flaskrun import flaskrun
from helloworld.libs.db_uttility import get_fut_code as get_fut_code_db
from helloworld.libs.type_convert import decimal_default

dynamodb = boto3.resource('dynamodb')
application = Flask(__name__)


@application.route('/', methods=['GET'])
def get():
    return Response(json.dumps({'Output': 'Hello World'}), mimetype='application/json', status=200)


@application.route('/', methods=['POST'])
def post():
    return Response(json.dumps({'Output': 'Hello World'}), mimetype='application/json', status=200)


@application.route('/future', methods=['GET'])
def get_future():
    table = dynamodb.Table("fut_code")
    response = table.scan()
    return Response(json.dumps(response['Items'], default=decimal_default), mimetype='application/json', status=200)


@application.route('/fut-code/<fut_code>', methods=['GET'])
def get_fut_code(fut_code):
    table = dynamodb.Table("fut_code")
    # response = table.get_item(Key={'fut_code': fut_code})
    # )
    response = table.query(
        KeyConditionExpression=Key('fut_code').eq(fut_code)

    )
    return Response(json.dumps(response['Items'], default=decimal_default), mimetype='application/json', status=200)


@application.route('/signal/<ts_code>', methods=['GET'])
def get_signal(ts_code):
    table = dynamodb.Table("signal")
    # response = table.get_item(Key={'fut_code': fut_code})
    # )
    response = table.query(
        KeyConditionExpression=Key('ts_code').eq(ts_code)

    )
    return Response(json.dumps(response['Items'], default=decimal_default), mimetype='application/json', status=200)


if __name__ == '__main__':
    flaskrun(application)
