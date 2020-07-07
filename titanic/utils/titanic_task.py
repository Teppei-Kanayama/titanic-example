import os
from typing import Optional

import gokart
import luigi
from gokart.file_processor import FileProcessor
from gokart.target import TargetOnKart


class Titanic(gokart.TaskOnKart):
    task_namespace = 'titanic'

    # local_workspace_directory: str = luigi.Parameter()

    def make_local_target(self, relative_file_path: str, use_unique_id: bool = True, processor: Optional[FileProcessor] = None) -> TargetOnKart:
        file_path = os.path.join('hoge', relative_file_path)
        unique_id = self.make_unique_id() if use_unique_id else None
        return gokart.target.make_target(file_path=file_path, unique_id=unique_id, processor=processor)
