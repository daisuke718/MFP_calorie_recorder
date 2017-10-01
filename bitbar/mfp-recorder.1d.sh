#!/usr/bin/env bash

dirname=`dirname $0`
realpath=`dirname $(readlink $0)`
abs_path=$(cd $dirname;cd $realpath;pwd)

echo '| image=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'
echo '---'
echo "regist calorie | bash=$abs_path/../exec_recorder.sh;exit;"
echo 'open myfitnesspal | href=http://www.myfitnesspal.com/food/diary'
echo '---'
echo 'edit script | bash="vim $0;exit;"'
