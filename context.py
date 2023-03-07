import time


class RuntimeContext(object):
    def __init__(
            self,
            function_name: str,
            function_version: str,
            memory_limit_in_mb: str,
            request_id: str,
            deadline_ms: str,
            token: dict = None,
    ):
        self.function_name = function_name
        self.function_version = function_version
        self.memory_limit_in_mb = int(memory_limit_in_mb)
        self.request_id = request_id
        self.deadline_ms = int(deadline_ms)
        self.token = token

    def get_remaining_time_in_millis(self):
        return self.deadline_ms - int(round(time.time() * 1000))


def context_example():
    return RuntimeContext(
        function_name='d4eo2faf62**********',
        function_version='d4e3vrugh3**********',
        memory_limit_in_mb='128',
        request_id='6e8356f9-489b-4c7b-8ba6-c8cd74f25455',
        deadline_ms=str(int(round(time.time() * 1000)) + 10),
    )
