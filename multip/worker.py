import time
import custom_logging
import os
from typing import Sequence

# use this to overwrite print before all other scripts
print = custom_logging.print

def process_entry(value: str, method: str, interval: int, repeat: int, log_file_path: str):
    custom_logging.setup_logging(log_file_path)
    for i in range(repeat):
        time.sleep(interval)
        print(f'Entry {value}@{method}: {i} of {repeat}')

# the following will run when you are running this file as entry.
if __name__ == '__main__':
    from absl import flags, app
    VALUE = flags.DEFINE_string('value', 'jack', 'the name of person')
    METHOD = flags.DEFINE_string('method', 'sleep', 'the action to do')
    INTERVAL = flags.DEFINE_integer('interval', 3, 'interval between actions')
    REPEAT = flags.DEFINE_integer('repeat', 5, 'how many repeats of actions')
    LOG_FILE_PATH = flags.DEFINE_string(
        'log_file_path',
        os.path.join(os.getenv('PYTHONPATH'), 'logs', 'main-entry-logs.log'),
        'where to log')
    def main(argv: Sequence[str]):
        process_entry(VALUE.value, METHOD.value, INTERVAL.value, REPEAT.value, LOG_FILE_PATH.value)
    app.run(main)
