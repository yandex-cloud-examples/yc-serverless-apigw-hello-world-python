import json
import sys

from context import RuntimeContext, context_example
from handler import handler


def main():
    if len(sys.argv) != 2 and len(sys.argv) != 3:
        print("Usage: python main.py <json event> [<json context>]")
        return

    event_json = sys.argv[1]
    context_json = sys.argv[2] if len(sys.argv) == 3 else None
    try:
        event = json.loads(event_json)
        parsed_context = json.loads(context_json)
        context = context_example() if context_json is None else RuntimeContext(
            function_name=parsed_context['functionName'],
            function_version=parsed_context['functionVersion'],
            memory_limit_in_mb=parsed_context['memoryLimitInMB'],
            request_id=parsed_context['requestId'],
            deadline_ms=parsed_context['deadlineMs'],
            token=parsed_context.get('token'),
        )
    except json.JSONDecodeError as e:
        print(f'JSON parsing error: {e.msg}')
        return
    except KeyError as e:
        print(f'JSON parsing error: {e}')
        return

    try:
        print(json.dumps(handler(event, context)))
    except Exception as e:
        print(f'Handler error: {e}')


if __name__ == '__main__':
    main()
