import os
import shutil
import unittest

import svn.constants
import svn.exception
import svn.remote
import svn.test_support


def onerror(func, path, exc_info):
    import stat

    if not os.access(path, os.W_OK):
        # Is the error an access error ?
        os.chmod(path, stat.S_IWUSR)
        func(path)
    else:
        raise


class TestRemoteClient(unittest.TestCase):
    """
    For testing svn/remote.py
    """

    def shortDescription(self):
        return None

    def setUp(self):
        self.test_svn_url = "http://svn.apache.org/repos/asf/ace/trunk/cnf/lib/kxml2"
        self.test_fake_url = "http://svn_abc.1apache.org1/repos/asf/src"
        self.test_start_revision = 1760022
        self.test_end_revision = 1760023

    def tearDown(self):
        if os.path.exists("trial"):
            shutil.rmtree("trial", onerror=onerror)

    def test_error_client_formation(self):
        try:
            svn.remote.RemoteClient(self.test_fake_url).checkout(".")
        except svn.exception.SvnException:
            pass
        else:
            raise Exception("Expected exception for bad URL.")

    def test_checkout(self):
        """
        Testing checkout
        :return:
        """
        shutil.rmtree("trial", ignore_errors=True, onerror=onerror)
        svn.remote.RemoteClient(self.test_svn_url).checkout("trial")
        self.assertTrue(os.path.exists("trial"))

    def test_remove(self):
        with svn.test_support.temp_repo() as (_, rc):
            with svn.test_support.temp_checkout():
                svn.test_support.populate_bigger_file_changes1()

            current_entries = rc.list()
            current_entries = list(current_entries)

            self.assertIn("new_file", current_entries)

            # Confirm it's there.

            current_entries = rc.list()
            current_entries = list(current_entries)

            self.assertIn("new_file", current_entries)

            # Remove.

            rc.remove("new_file", "Remove file.")

            # Confirm that it's gone.

            current_entries = rc.list()
            current_entries = list(current_entries)

            self.assertNotIn("new_file", current_entries)
