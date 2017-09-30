#!/usr/bin/env bash

CURRENT_DIR=`dirname $0`
cd ${CURRENT_DIR}
source bin/activate
pip-compile requirements/requirements.in > requirements/requirements.txt
