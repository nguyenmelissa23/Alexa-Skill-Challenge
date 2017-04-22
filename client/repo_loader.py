class RepoLoader:
    def __init__(self, filename):
        self.filename = filename
        self.repositories = {}
        with open(filename, 'r') as repo_file:
            for path in repo_file:
                repo_name = str(path.split('\\')[-1]).rstrip()
                self.repositories[repo_name] = str(path).rstrip()
            repo_file.close()

    def get_names(self):
        return list(self.repositories.keys())

    def get_path(self, name):
        return self.repositories[name]

    def get_all(self):
        return self.repositories