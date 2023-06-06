SHELL := /bin/bash

all: setup pre task post

clean:
	# make clean
	# Drop vehicles table
	python3 ./clean.py

setup:
	# make setup
	# Create vehicles table
	python3 ./setup.py

pre:
	# make pre
	# Test that vehicles table exists
	python3 ./test_db.py

task:
	# make task
	# Clean vehicles data and insert into vehicles table
	python3 ./task.py

post:
	# make post
	# Confirm vehicles table has rows
	python3 ./post.py