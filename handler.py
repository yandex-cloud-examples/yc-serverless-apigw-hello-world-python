def handler(event, context):
    try:
        operation_context = event['requestContext']['apiGateway']['operationContext']
    except KeyError:
        return error(500, 'undefined command context')

    try:
        name = operation_context['name']
    except KeyError:
        return error(500, 'undefined command name')

    return response(f'Hello, {name}!')


def error(code, message):
    return {
        'statusCode': code,
        'body': {'message': message},
        'isBase64Encoded': False,
    }


def response(body):
    return {
        'statusCode': 200,
        'body': body,
        'isBase64Encoded': False,
    }
