import json
import base64
import io
from PIL import Image

QUERY_STRING_PARAMETERS = 'queryStringParameters'

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

    # パラメタの取得
    width = (int)(event.get(QUERY_STRING_PARAMETERS).get('width') or 512)
    height = (int)(event.get(QUERY_STRING_PARAMETERS).get('height') or 512)
    x_min = (float)(event.get(QUERY_STRING_PARAMETERS).get('x_min') or -2.2)
    x_max = (float)(event.get(QUERY_STRING_PARAMETERS).get('x_max') or 1.8)
    y_min = (float)(event.get(QUERY_STRING_PARAMETERS).get('y_min') or -2.0)
    y_max = (float)(event.get(QUERY_STRING_PARAMETERS).get('y_max') or 2.0)
    iterations = (int)(event.get(QUERY_STRING_PARAMETERS).get('iterations') or 100)
    threshold = (int)(event.get(QUERY_STRING_PARAMETERS).get('threshold') or 10)

    # 画像を作成
    image = Image.new('RGB', (width, height), (0, 0, 0))

    # マンデルブロ集合を描写
    for x in range(width):
        for y in range(height):
            # 座標を計算
            c = complex(x_min + (x_max - x_min) * x / width, y_min + (y_max - y_min) * y / height)
            z = 0.0j
            # マンデルブロ集合の計算
            for i in range(iterations):
                z = z * z + c
                if (z.real * z.real + z.imag * z.imag) >= threshold:
                    break
            # 色を決定
            if i >= iterations - 1:
                image.putpixel((x, y), (0, 0, 0))
            else:
                image.putpixel((x, y), (255, 255, 255))

    # 画像をバイトデータに変換
    with io.BytesIO() as output:
        image.save(output, format="png")
        image_data = output.getvalue()

    # Base64エンコード
    encoded_image_data = base64.b64encode(image_data)

    # 画像を返す
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "image/png"
        },
        "body": encoded_image_data,
        "isBase64Encoded": True
    }
