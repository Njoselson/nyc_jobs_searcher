from typing import Optional
from pydantic import BaseModel


class JobPosting(BaseModel):
    job_id: int
    agency: str
    posting_type: str
    number_of_positions: int
    business_title: str
    civil_service_title: str
    title_classification: str
    title_code_no: str
    level: str
    job_category: str
    career_level: str
    salary_range_from: str
    salary_range_to: str
    salary_frequency: str
    work_location: str
    division_work_unit: str
    job_description: str
    to_apply: str
    residency_requirement: str
    posting_date: str
    posting_updated: str
    process_date: str
    minimum_qual_requirements: Optional[str] = None
    full_time_part_time_indicator: Optional[str] = None
    preferred_skills: Optional[str] = None
    additional_information: Optional[str] = None
    hours_shift: Optional[str] = None
    work_location_1: Optional[str] = None
    recruitment_contact: Optional[str] = None
    post_until: Optional[str] = None
