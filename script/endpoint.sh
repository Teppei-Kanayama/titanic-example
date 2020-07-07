#!/usr/bin/env bash

set -euC

python main.py titanic.SampleTask --local-scheduler
kaggle competitions submit -c titanic -f ./local_resources/submission.csv -m "Message"
