### 事前に必要なパッケージ
- pipenv

### local環境での実行手順
-  ライブラリのインストール
```bash
pipenv install
```
- `conf/env.list.sample`を参考に、環境変数を設定する
-  上で指定したs3バケットの`/input/`に、titanicの`train.csv`, `test.csv`, `gender_submission.csv`を配置する
-  下記コマンドを実行する
```bash
bash script/endpoint.sh
```
