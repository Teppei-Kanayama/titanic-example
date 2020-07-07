import pandas as pd
import luigi

from titanic.utils.titanic_task import Titanic


class LoadData(Titanic):
    task_namespace = 'titanic'

    file_path: str = luigi.Parameter()

    def output(self):
        return self.make_target(self.file_path, use_unique_id=False)


class SampleTask(Titanic):
    task_namespace = 'titanic'

    rerun = True

    def output(self):
        return dict(submission=self.make_target('submission.csv'),
                    submission_local=self.make_local_target('submission.csv', use_unique_id=False))

    def requires(self):
        return dict(sample_submission=LoadData(file_path='input/gender_submission.csv'),
                    train=LoadData(file_path='input/train.csv'),
                    test=LoadData(file_path='input/test.csv'))

    def run(self):
        sample_submission = self.load_data_frame('sample_submission', required_columns={'PassengerId', 'Survived'})
        train = self.load_data_frame('train')
        test = self.load_data_frame('test')
        output = self._run(sample_submission, train, test)
        self.dump(output, 'submission')
        self.dump(output, 'submission_local')

    @staticmethod
    def _run(sample_submission: pd.DataFrame, train: pd.DataFrame, test: pd.DataFrame) -> pd.DataFrame:
        # TODO: do somithing!
        return sample_submission
