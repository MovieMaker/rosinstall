import sys
from StringIO import StringIO
from rosinstall.rosinstall_cli import rosinstall_main
from rosinstall.rosws_cli import rosws_main
from test.scm_test_base import AbstractSCMTest, _add_to_file, _nth_line_split
        cmd = ["rosinstall", "ws", "-n"]
        os.chdir(self.test_root_path)
        rosinstall_main(cmd)
        cmd = ["rosinstall", "ws", "--diff"]
        os.chdir(self.test_root_path)
        sys.stdout = output = StringIO();
        rosinstall_main(cmd)
        sys.stdout = sys.__stdout__
        output = output.getvalue()
        cmd = ["rosws", "diff", "-t", "ws"]
        os.chdir(self.test_root_path)
        sys.stdout = output = StringIO();
        rosws_main(cmd)
        sys.stdout = sys.__stdout__
        output = output.getvalue()
        cmd = ["rosinstall", ".", "--diff"]
        os.chdir(directory)
        sys.stdout = output = StringIO();
        rosinstall_main(cmd)
        output = output.getvalue()
        cmd = ["rosws", "diff"]
        os.chdir(directory)
        sys.stdout = output = StringIO();
        rosws_main(cmd)
        output = output.getvalue()
        sys.stdout = sys.__stdout__
        cmd = ["rosinstall", ".", "--status"]
        os.chdir(directory)
        sys.stdout = output = StringIO();
        rosinstall_main(cmd)
        output = output.getvalue()
        cmd = ["rosws", "status"]
        os.chdir(directory)
        sys.stdout = output = StringIO();
        rosws_main(cmd)
        output = output.getvalue()
        sys.stdout = sys.__stdout__
        cmd = ["rosinstall", "ws", "--status"]
        os.chdir(self.test_root_path)
        sys.stdout = output = StringIO();
        rosinstall_main(cmd)
        sys.stdout = output = StringIO();
        rosinstall_main(cmd)
        sys.stdout = sys.__stdout__
        output = output.getvalue()
        cmd = ["rosws", "status", "-t", "ws"]
        os.chdir(self.test_root_path)
        sys.stdout = output = StringIO();
        rosws_main(cmd)
        sys.stdout = sys.__stdout__
        output = output.getvalue()
        cmd = ["rosinstall", "ws", "--status-untracked"]
        os.chdir(self.test_root_path)
        sys.stdout = output = StringIO();
        rosinstall_main(cmd)
        sys.stdout = sys.__stdout__
        output = output.getvalue()
        cmd = ["rosws", "status", "-t", "ws", "--untracked"]
        os.chdir(self.test_root_path)
        sys.stdout = output = StringIO();
        rosws_main(cmd)
        sys.stdout = sys.__stdout__
        output = output.getvalue()
        cmd = ["rosws", "info", "-t", "ws"]
        os.chdir(self.test_root_path)
        sys.stdout = output = StringIO();
        rosws_main(cmd)
        output = output.getvalue()
	cmd = ["rosws", "update"]
        os.chdir(self.local_path)
        sys.stdout = output = StringIO();
        rosws_main(cmd)
        output = output.getvalue()
	sys.stdout = sys.__stdout__
	cmd = ["rosws", "info", "-t", "ws"]
        os.chdir(self.test_root_path)
        sys.stdout = output = StringIO();
        rosws_main(cmd)
        output = output.getvalue()
        os.chdir(self.test_root_path)
        sys.stdout = output = StringIO();
        rosws_main(cmd)
        output = output.getvalue()
        tokens = _nth_line_split(-2, output)
        os.chdir(self.test_root_path)
        sys.stdout = output = StringIO();
        rosws_main(cmd)
        output = output.getvalue()
        tokens = _nth_line_split(-2, output)
        os.chdir(self.test_root_path)
        sys.stdout = output = StringIO();
        rosws_main(cmd)
        output = output.getvalue()
        tokens = _nth_line_split(-2, output)