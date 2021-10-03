import multiprocessing
import worker
import os
import datetime
from typing import List
from termcolor import colored

def get_available_log_file(base_file_name: str):
    i = 0
    while os.path.isfile(base_file_name + '-' + str(i).rjust(4, '0') + '.log'):
        i += 1
    return base_file_name + '-' + str(i).rjust(4, '0') + '.log'

def run_multiple_workers(base_path: str):
    # create the log dir
    log_dir = os.path.join(base_path, 'logs')
    if not os.path.isdir(log_dir):
        os.mkdir(log_dir)
    date = datetime.datetime.utcnow().strftime('%Y-%m-%d')
    interval = 3
    repeat = 5
    processes: List[multiprocessing.Process] = []
    for value in ['alice', 'bob', 'cinderella']:
        for method in ['dance', 'jump', 'leap']:
            log_file = get_available_log_file(os.path.join(log_dir, f'{date}-{value}-{method}'))
            print(
                colored('Run Worker:', 'green'),
                colored('value=', 'yellow') + colored(value, 'magenta'),
                colored('method=', 'yellow') + colored(method, 'magenta'),
                colored('log=', 'yellow') + colored(log_file, 'magenta')
            )
            process = multiprocessing.Process(
                target=worker.process_entry,
                args=(value, method, interval, repeat, log_file)
            )
            process.start()
            processes.append(process)
    for process in processes:
        process.join()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    base_path = os.getenv('PYTHONPATH')
    run_multiple_workers(base_path=base_path)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
