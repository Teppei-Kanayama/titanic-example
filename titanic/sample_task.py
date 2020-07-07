import pandas as pd
import gokart
import luigi


class LoadData(gokart.TaskOnKart):
    task_namespace = 'titanic'

    file_path: str = luigi.Parameter()

    def output(self):
        return self.make_target(self.file_path, use_unique_id=False)


class SampleTask(gokart.TaskOnKart):
    task_namespace = 'titanic'

    def output(self):
        return self.make_target('submission.csv')

    def requires(self):
        return dict(sample_submission=LoadData(file_path='input/gender_submission.csv'),
                    train=LoadData(file_path='input/train.csv'),
                    test=LoadData(file_path='input/test.csv'))

    def run(self):
        sample_submission = self.load_data_frame('sample_submission', required_columns={'PassengerId', 'Survived'})
        train = self.load_data_frame('train')
        test = self.load_data_frame('test')
        output = self._run(sample_submission, train, test)
        self.dump(output)

    @staticmethod
    def _run(sample_submission: pd.DataFrame, train: pd.DataFrame, test: pd.DataFrame) -> pd.DataFrame:
        # TODO: do somithing!
        return sample_submission
