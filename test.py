import unittest

from context import context_example
from handler import handler


class TestHandler(unittest.TestCase):
    def test_handler(self):
        requestId = 'a2fe3b91-4efe-4a59-b916-ce1b6b004142'
        event = {
            'requestContext': {
                'identity': {
                    'sourceIp': '2a02:6b8:c02:900:0:f822:0:a8',
                    'userAgent': 'PostmanRuntime/7.28.1',
                },
                'httpMethod': 'GET',
                'requestId': requestId,
                'requestTime': '24/Aug/2021:17:48:59 +0000',
                'requestTimeEpoch': 1_629_827_339,
                'apiGateway': {
                    'operationContext': {
                        'name': 'world',
                    },
                },
            },
            'httpMethod': 'GET',
            'path': '/world',
            'isBase64Encoded': False,
        }
        context = context_example()

        response = handler(event, context)

        self.assertEqual(response['statusCode'], 200)
        self.assertEqual(response['body'], "Hello, world!")


if __name__ == "__main__":
    unittest.main()
