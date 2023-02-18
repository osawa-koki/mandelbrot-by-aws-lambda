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

    try:
        # パラメタの取得
        # width = (int)(event.get(QUERY_STRING_PARAMETERS).get('width') or 512)
        # height = (int)(event.get(QUERY_STRING_PARAMETERS).get('height') or 512)
        # x_min = (float)(event.get(QUERY_STRING_PARAMETERS).get('x_min') or -2.2)
        # x_max = (float)(event.get(QUERY_STRING_PARAMETERS).get('x_max') or 1.8)
        # y_min = (float)(event.get(QUERY_STRING_PARAMETERS).get('y_min') or -2.0)
        # y_max = (float)(event.get(QUERY_STRING_PARAMETERS).get('y_max') or 2.0)
        # iterations = (int)(event.get(QUERY_STRING_PARAMETERS).get('iterations') or 100)
        # threshold = (int)(event.get(QUERY_STRING_PARAMETERS).get('threshold') or 10)

        width = 512
        height = 512
        x_min = -2.5
        x_max = 1.5
        y_min = -2.0
        y_max = 2.0
        iterations = 100
        threshold = 10

        # 画像を作成
        image = Image.new('RGB', (width, height), (0, 0, 0))

        for py in range(height):
            y = py / height * (y_max - y_min) + y_min
            for px in range(width):
                x = px / width * (x_max - x_min) + x_min
                z = complex(x, y)
                v = complex(0, 0)
                color = 0
                for n in range(iterations):
                    v = v * v + z
                    if abs(v) > threshold:
                        color = 255 - threshold * n
                        break
                image.putpixel((px, py), (color, color, color))

        # 画像をBASE64エンコード
        buffered = io.BytesIO()
        image.save(buffered, format="PNG")
        encoded_image_data = base64.b64encode(buffered.getvalue()).decode('utf-8')

        # 画像を返す
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "image/png",
            },
            "body": encoded_image_data,
            "isBase64Encoded": True,
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({
                "message": str(e),
            }),
        }
