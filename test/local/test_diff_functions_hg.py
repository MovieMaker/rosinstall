def create_hg_repo(remote_path):
    # create a "remote" repo
    subprocess.check_call(["hg", "init"], cwd=remote_path)
    subprocess.check_call(["touch", "fixed.txt"], cwd=remote_path)
    subprocess.check_call(["touch", "modified.txt"], cwd=remote_path)
    subprocess.check_call(["touch", "modified-fs.txt"], cwd=remote_path)
    subprocess.check_call(["touch", "deleted.txt"], cwd=remote_path)
    subprocess.check_call(["touch", "deleted-fs.txt"], cwd=remote_path)
    subprocess.check_call(["hg", "add", "fixed.txt"], cwd=remote_path)
    subprocess.check_call(["hg", "add", "modified.txt"], cwd=remote_path)
    subprocess.check_call(["hg", "add", "modified-fs.txt"], cwd=remote_path)
    subprocess.check_call(["hg", "add", "deleted.txt"], cwd=remote_path)
    subprocess.check_call(["hg", "add", "deleted-fs.txt"], cwd=remote_path)
    subprocess.check_call(["hg", "commit", "-m", "modified"], cwd=remote_path)

def modify_hg_repo(clone_path):
    # make local modifications
    subprocess.check_call(["rm", "deleted-fs.txt"], cwd=clone_path)
    subprocess.check_call(["hg", "rm", "deleted.txt"], cwd=clone_path)
    _add_to_file(os.path.join(clone_path, "modified-fs.txt"), u"foo\n")
    _add_to_file(os.path.join(clone_path, "modified.txt"), u"foo\n")
    _add_to_file(os.path.join(clone_path, "added-fs.txt"), u"tada\n")
    _add_to_file(os.path.join(clone_path, "added.txt"), u"flam\n")
    subprocess.check_call(["hg", "add", "added.txt"], cwd=clone_path)

        create_hg_repo(remote_path)
        modify_hg_repo(clone_path)
        self.assertEqual('diff --git clone/added.txt clone/added.txt\nnew file mode 100644\n--- /dev/null\n+++ clone/added.txt\n@@ -0,0 +1,1 @@\n+flam\ndiff --git clone/deleted.txt clone/deleted.txt\ndeleted file mode 100644\ndiff --git clone/modified-fs.txt clone/modified-fs.txt\n--- clone/modified-fs.txt\n+++ clone/modified-fs.txt\n@@ -0,0 +1,1 @@\n+foo\ndiff --git clone/modified.txt clone/modified.txt\n--- clone/modified.txt\n+++ clone/modified.txt\n@@ -0,0 +1,1 @@\n+foo\n', output)
        self.assertEqual('M       clone/modified-fs.txt\nM       clone/modified.txt\nA       clone/added.txt\nR       clone/deleted.txt\n!       clone/deleted-fs.txt\n', output)
        self.assertEqual('M       clone/modified-fs.txt\nM       clone/modified.txt\nA       clone/added.txt\nR       clone/deleted.txt\n!       clone/deleted-fs.txt\n', output)
        self.assertEqual('M       clone/modified-fs.txt\nM       clone/modified.txt\nA       clone/added.txt\nR       clone/deleted.txt\n!       clone/deleted-fs.txt\n', output)
        self.assertEqual('M       clone/modified-fs.txt\nM       clone/modified.txt\nA       clone/added.txt\nR       clone/deleted.txt\n!       clone/deleted-fs.txt\n', output)
        self.assertEqual('M       clone/modified-fs.txt\nM       clone/modified.txt\nA       clone/added.txt\nR       clone/deleted.txt\n!       clone/deleted-fs.txt\n?       clone/added-fs.txt\n', output)
        self.assertEqual('M       clone/modified-fs.txt\nM       clone/modified.txt\nA       clone/added.txt\nR       clone/deleted.txt\n!       clone/deleted-fs.txt\n?       clone/added-fs.txt\n', output)