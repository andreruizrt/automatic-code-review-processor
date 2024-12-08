from test import test_github_wrapper


class ProcessorTest():
    def __init__(self):
        self.testWrapper = test_github_wrapper.TestGitHubWrapper()

    def run_all_tests(self):
        self.testWrapper.test_get_id_project_source_by_id_project_target()


if __name__ == "__main__":
    processorTest = ProcessorTest()
    processorTest.run_all_tests()
