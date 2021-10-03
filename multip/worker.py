import time
import custom_logging

# use this to overwrite print before all other scripts
print = custom_logging.print

def process_entry(value: str, method: str, interval: int, repeat: int, log_file_path: str):
    custom_logging.setup_logging(log_file_path)
    for i in range(repeat):
        time.sleep(interval)
        print(f'Entry {value}@{method}: {i} of {repeat}')
