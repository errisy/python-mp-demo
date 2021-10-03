import logging

rootLogger = logging.getLogger()

# overwrite the print method in
def print(*kwargs):
    rootLogger.info(*kwargs)


def setup_logging(log_file_path: str):
    logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")

    fileHandler = logging.FileHandler(log_file_path)
    fileHandler.setFormatter(logFormatter)
    rootLogger.addHandler(fileHandler)

    consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(logFormatter)
    rootLogger.addHandler(consoleHandler)

    rootLogger.setLevel(logging.DEBUG)

    print(f'Work Log => {log_file_path}')