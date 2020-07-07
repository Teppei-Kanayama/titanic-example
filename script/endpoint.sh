#!/usr/bin/env bash

set -euC

python main.py titanic.SampleTask --local-scheduler
kaggle competitions submit -c titanic -f submission.csv -m "Message"
