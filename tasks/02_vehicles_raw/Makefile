SHELL := /bin/bash

all: setup pre task post

clean:
	# make clean
	# Drop vehicles_raw table
	python3 ./clean.py

setup:
	# make setup
	# Create vehicles_raw table
	python3 ./setup.py

pre:
	# make pre
	# Test that vehicles_raw table exists
	python3 ./test_db.py

task:
	# make task
	# Insert vehicles_raw data into vehicles_raw table
	python3 ./task.py

post:
	# make post
	# Confirm vehicles_raw table has rows
	python3 ./post.py