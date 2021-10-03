from absl.testing import absltest
import worker
import os
import sys
import test_util

class TestWorker(absltest.TestCase):

    def test_process_entry(self):
        test_log_file_name = os.path.join(test_util.get_tmp_dir(), 'test-run-log.log')
        print('log file is:', test_log_file_name)
        if os.path.isfile(test_log_file_name):
            os.remove(test_log_file_name)
        worker.process_entry(
            value='jack',
            method='test',
            interval=0.1,
            repeat=10,
            log_file_path=test_log_file_name
        )
        with open(test_log_file_name, 'r') as log_file:
            logs = log_file.read()
        print('logs:', logs)
        self.assertTrue(f'Work Log => {test_log_file_name}' in logs)
        # clean up
        if os.path.isfile(test_log_file_name):
            os.remove(test_log_file_name)

if __name__ == '__main__':
    absltest.main()