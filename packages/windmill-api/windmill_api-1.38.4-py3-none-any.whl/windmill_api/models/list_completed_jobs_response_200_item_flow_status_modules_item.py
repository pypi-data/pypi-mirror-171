from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.list_completed_jobs_response_200_item_flow_status_modules_item_branch_chosen import (
    ListCompletedJobsResponse200ItemFlowStatusModulesItemBranchChosen,
)
from ..models.list_completed_jobs_response_200_item_flow_status_modules_item_iterator import (
    ListCompletedJobsResponse200ItemFlowStatusModulesItemIterator,
)
from ..models.list_completed_jobs_response_200_item_flow_status_modules_item_type import (
    ListCompletedJobsResponse200ItemFlowStatusModulesItemType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ListCompletedJobsResponse200ItemFlowStatusModulesItem")


@attr.s(auto_attribs=True)
class ListCompletedJobsResponse200ItemFlowStatusModulesItem:
    """ """

    type: ListCompletedJobsResponse200ItemFlowStatusModulesItemType
    job: Union[Unset, str] = UNSET
    count: Union[Unset, int] = UNSET
    iterator: Union[Unset, ListCompletedJobsResponse200ItemFlowStatusModulesItemIterator] = UNSET
    forloop_jobs: Union[Unset, List[str]] = UNSET
    branch_chosen: Union[Unset, ListCompletedJobsResponse200ItemFlowStatusModulesItemBranchChosen] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        job = self.job
        count = self.count
        iterator: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.iterator, Unset):
            iterator = self.iterator.to_dict()

        forloop_jobs: Union[Unset, List[str]] = UNSET
        if not isinstance(self.forloop_jobs, Unset):
            forloop_jobs = self.forloop_jobs

        branch_chosen: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.branch_chosen, Unset):
            branch_chosen = self.branch_chosen.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )
        if job is not UNSET:
            field_dict["job"] = job
        if count is not UNSET:
            field_dict["count"] = count
        if iterator is not UNSET:
            field_dict["iterator"] = iterator
        if forloop_jobs is not UNSET:
            field_dict["forloop_jobs"] = forloop_jobs
        if branch_chosen is not UNSET:
            field_dict["branch_chosen"] = branch_chosen

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = ListCompletedJobsResponse200ItemFlowStatusModulesItemType(d.pop("type"))

        job = d.pop("job", UNSET)

        count = d.pop("count", UNSET)

        iterator: Union[Unset, ListCompletedJobsResponse200ItemFlowStatusModulesItemIterator] = UNSET
        _iterator = d.pop("iterator", UNSET)
        if not isinstance(_iterator, Unset):
            iterator = ListCompletedJobsResponse200ItemFlowStatusModulesItemIterator.from_dict(_iterator)

        forloop_jobs = cast(List[str], d.pop("forloop_jobs", UNSET))

        branch_chosen: Union[Unset, ListCompletedJobsResponse200ItemFlowStatusModulesItemBranchChosen] = UNSET
        _branch_chosen = d.pop("branch_chosen", UNSET)
        if not isinstance(_branch_chosen, Unset):
            branch_chosen = ListCompletedJobsResponse200ItemFlowStatusModulesItemBranchChosen.from_dict(_branch_chosen)

        list_completed_jobs_response_200_item_flow_status_modules_item = cls(
            type=type,
            job=job,
            count=count,
            iterator=iterator,
            forloop_jobs=forloop_jobs,
            branch_chosen=branch_chosen,
        )

        list_completed_jobs_response_200_item_flow_status_modules_item.additional_properties = d
        return list_completed_jobs_response_200_item_flow_status_modules_item

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
