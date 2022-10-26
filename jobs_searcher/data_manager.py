from typing import Optional, Any, List
import random

import requests

from jobs_searcher.models import JobPosting
from jobs_searcher.utils.common_logger import LOGGER


class JobsDataManager:
    def __init__(self) -> None:
        self.job_list: Optional[List[Any]] = None
        self.jobs_data_api_gateway: str = (
            "https://data.cityofnewyork.us/resource/kpav-sd4t.json"
        )

    def fetch_new_data(self) -> None:
        LOGGER.info(f"Fetching new data from {self.jobs_data_api_gateway}")
        response = requests.get(self.jobs_data_api_gateway)
        self.job_list = [JobPosting(**json_str) for json_str in response.json()]

    def get_lucky(self) -> JobPosting:
        if self.job_list:
            return random.choice(self.job_list) 
        else:
            self.fetch_new_data()
            return random.choice(self.job_list) # type: ignore
