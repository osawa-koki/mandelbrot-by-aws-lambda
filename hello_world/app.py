import json
import base64
import io
from PIL import Image


def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    width = 200
    height = 200

    # 黒い画像を作成
    image = Image.new('RGB', (width, height), (0, 0, 0))

    # 画像をバイトデータに変換
    with io.BytesIO() as output:
        image.save(output, format="JPEG")
        image_data = output.getvalue()

    # Base64エンコード
    encoded_image_data = base64.b64encode(image_data).decode('utf-8')

    # 画像を返す
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "image/jpeg"
        },
        "body": encoded_image_data,
        "isBase64Encoded": True
    }
