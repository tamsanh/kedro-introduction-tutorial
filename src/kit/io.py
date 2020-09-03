from typing import Any, Dict

from kedro.io import AbstractDataSet


class ReplaceableDataSet(AbstractDataSet):

    def __init__(self):
        pass

    def _load(self) -> Any:
        raise Exception(f"Error: You are trying to run the pipeline without replacing the 'REPLACE_ME' dataset!")

    def _save(self, _):
        raise Exception(f"Error: You are trying to run the pipeline without replacing the 'REPLACE_ME' dataset!")

    def _describe(self) -> Dict[str, Any]:
        return dict()
