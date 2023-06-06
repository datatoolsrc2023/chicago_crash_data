SHELL := /bin/bash

all: setup pre task post

clean:
	# make clean
	# Drop crashes_raw table
	python3 ./clean.py

setup:
	# make setup
	# Create crashes_raw table
	python3 ./setup.py

pre:
	# make pre
	# Test that crashes_raw table exists
	python3 ./test_db.py

task:
	# make task
	# Insert crashes_raw data into crashes_raw table
	python3 ./task.py

post:
	# make post
	# Confirm crashes_raw table has rows
	python3 ./post.py