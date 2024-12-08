import unittest

from infra.git.github.github_wrapper import GitHubWrapper


class TestGitHubWrapper(unittest.TestCase):

    def __init__(self, methodName='runTest'):
        super().__init__(methodName)
        self.git_url = 'https://github.com.br'
        self.git_token = 'API_TOKEN'
        self.wrapper = GitHubWrapper(
            git_url=self.git_url, git_token=self.git_token)

    def test_get_http_url_by_project_id(self):
        result = self.wrapper.get_http_url_by_project_id(778542693)
        self.assertEqual(
            result, 'https://github.com/andreruizrt/redes-neurais')

    def test_get_id_project_source_by_id_project_target(self):
        id_project_base = 778542693
        id_project_head = 778542693
        id_pull_request = 1
        result = self.wrapper.get_id_project_source_by_id_project_target(
            id_project_base,
            id_pull_request)
        self.assertEqual(
            result, id_project_head)

    def test_get_changes_by_merge(self, id_merge_request, id_project):
        pass

    def test_get_merge_request(self, id_merge_request, id_project):
        pass

    def test_clone_repo(self, url, branch, path):
        pass

    def test_get_threads_by_merge_request(self, id_project, id_merge_request):
        pass

    def test_resolve_merge_request_thread(self, id_thread, id_project, merge_request_id):
        pass

    def test_create_merge_request_thread(self, comment, id_project, id_merge_request, position):
        pass

    def test_get_versions_by_merge_request(self, id_project, id_merge_request):
        pass

    def test_get_project_by_id_project(self, id_project):
        pass

    def test_get_commits_behind(self, id_project_target, branch_target, id_project_source, branch_source):
        pass
