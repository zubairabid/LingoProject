#!/bin/bash
#assumes you're using python3
mkdir out2
python pron_filter.py
cd out2
python heuristicAndAnnHelper.py > annotateThis
echo 'ANNOTATION STARTS HERE'
less annotateThis
echo 'YOU ARE DONE ANNOTATING I ASSUME'
python senderdat.py
