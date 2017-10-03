#!/usr/bin/env bash

CURRENT_DIR=`dirname $0`
cd ${CURRENT_DIR}
source bin/activate
src/open_diary.py

