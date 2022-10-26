import unittest
from typing import List
from jobs_searcher.data_manager import JobsDataManager
from jobs_searcher.models import JobPosting


class TestJobsDataManager(unittest.TestCase):
    def setUp(self):
        self.jobs_data_manager = JobsDataManager()

    def test_should_fetch_new_data(self):
        # Given the job list is empty
        self.assertIsNone(self.jobs_data_manager.job_list)
        # when we fetch new data
        self.jobs_data_manager.fetch_new_data()
        # Then the jobs list is not none
        self.assertIsNotNone(self.jobs_data_manager.job_list)

        # And it has populated a list of jobs
        self.assertIsInstance(self.jobs_data_manager.job_list, List)
        self.assertIsInstance(self.jobs_data_manager.job_list[0], JobPosting)

    def test_get_lucky_should_return_random_job(self):
        # given a list of jobs
        self.jobs_data_manager.fetch_new_data()

        # when we call get_lucky
        random_job = self.jobs_data_manager.get_lucky()
        random_job2 = self.jobs_data_manager.get_lucky()

        # then we get random jobs
        self.assertIsInstance(random_job, JobPosting)
        self.assertIsInstance(random_job2, JobPosting)

        # Which are different from each other
        self.assertNotEqual(random_job, random_job2)
