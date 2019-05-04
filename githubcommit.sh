#!/bin/bash

#cd linuxopg
git add *
git config --global user.email "lak@djhhadsten.dk"
git config --global user.name "lkaae2018"
echo Navn til commiten?
read commit
git commit -m $commit
git push
