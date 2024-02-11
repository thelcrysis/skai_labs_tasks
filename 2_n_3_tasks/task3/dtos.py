from pydantic import BaseModel, validator
from flask import Response, abort


class InterviewsRequest(BaseModel):
    start_times: list[int]
    end_times: list[int]

    @validator("end_times")
    def check_lengths_are_equal(cls, v, values, **kwargs):
        """
        Checks that every time interval has both start and end time.
        """
        if len(values["start_times"]) != len(v):
            abort(Response("Mismatching lengths of provided time lists", 400))
        return v


class MaxInterviewResponse(BaseModel):
    max_interviews: int
