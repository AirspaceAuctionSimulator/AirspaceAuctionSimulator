from enum import Enum


class AllocationReason(Enum):
    FIRST_ALLOCATION = "FIRST_ALLOCATION"
    REALLOCATION = "REALLOCATION"
    ALLOCATION_FAILED = "ALLOCATION_FAILED"
