from absl.testing import absltest
import os
import test_util
import main

class TestWorker(absltest.TestCase):

    def test_main(self):
        base_dir = os.path.join(test_util.get_tmp_dir(), 'multip-test_main')
        if os.path.isdir(base_dir):
           os.removedirs(base_dir)
        os.mkdir(base_dir)
        main.run_multiple_workers(test_util.get_tmp_dir())
        # to do by yourself:
        # you need to check if the log files are created, and clean them up

if __name__ == '__main__':
    absltest.main()