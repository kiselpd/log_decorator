from datetime import datetime

def logger(old_function):
    log_path = "main.log"

    def new_function(*args, **kwargs):
        log_list = []

        function_name = old_function.__name__
        function_args = f"args: {args}"
        function_kwargs = f"kwargs: {kwargs}"

        value = old_function(*args, **kwargs)

        function_time = str(datetime.now())[:-7]
        function_value = f"return: {value}"

        with open(file=log_path, mode="a") as f:
            f.write(f"{function_name} | {function_time} | {function_args} | {function_kwargs} | {function_value}\n")

        return value
    
    return new_function


def smart_logger(file_path):

    def logger_(old_function):
        log_path = file_path

        def new_function(*args, **kwargs):
            log_list = []

            function_name = old_function.__name__
            function_args = f"args: {args}"
            function_kwargs = f"kwargs: {kwargs}"

            value = old_function(*args, **kwargs)

            function_time = str(datetime.now())[:-7]
            function_value = f"return: {value}"

            with open(file=log_path, mode="a") as f:
                f.write(f"{function_name} | {function_time} | {function_args} | {function_kwargs} | {function_value}\n")

            return value
    
        return new_function
    
    return logger_
