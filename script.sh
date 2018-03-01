#!/bin/bash
for filename in ./samples/*; do
	python2.7 hashcode.py $filename
done