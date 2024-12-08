import github

from infra.git.git_wrapper import GitWrapper


# TODO IMPLEMENTAR CLASSE
class GitHubWrapper(GitWrapper):

    def __init__(self, git_url, git_token):
        self.git_url = git_url
        self.git_token = git_token
        self.github_api = github.Github(git_token)

    def get_http_url_by_project_id(self, id_project):
        return self.github_api.get_repo(id_project).html_url

    def get_id_project_source_by_id_project_target(self, id_project_target, id_merge_request):
        pass

    def get_changes_by_merge(self, id_merge_request, id_project):
        pass

    def get_merge_request(self, id_merge_request, id_project):
        pass

    def clone_repo(self, url, branch, path):
        pass

    def get_threads_by_merge_request(self, id_project, id_merge_request):
        pass

    def resolve_merge_request_thread(self, id_thread, id_project, merge_request_id):
        pass

    def create_merge_request_thread(self, comment, id_project, id_merge_request, position):
        pass

    def get_versions_by_merge_request(self, id_project, id_merge_request):
        pass

    def get_project_by_id_project(self, id_project):
        pass

    def get_commits_behind(self, id_project_target, branch_target, id_project_source, branch_source):
        pass
