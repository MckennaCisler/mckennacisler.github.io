#!/usr/bin/env bash
THEME_DIR=../../../../Coding/project/jsonresume-theme-concise/
cp resume.json $THEME_DIR
cd $THEME_DIR
resume serve & # --theme=concise &
sleep 5
pkill -f $(which resume)
cd -
cp $THEME_DIR/public/index.html ./

