import os

class RepoLoader:
    def __init__(filename):
        self.filename = filename
        self.repositories = []
        with os.open(filename, 'r') as repo_file:
            for path in repo_file:
                repo_name = path.split('\')[-1]
                self.repositories[repo_name] = repo_file
            repo_file.close()

    def get_names():
        return list(self.repositories.keys())

    def get_path(name):
        return self.repositories[name]

    def get_all():
        return self.repositories