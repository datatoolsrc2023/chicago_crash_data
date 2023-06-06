SHELL := /bin/bash

all: setup pre task post

clean:
	# make clean
	# Drop crashes table
	python3 ./clean.py

setup:
	# make setup
	# Create crashes table
	python3 ./setup.py

pre:
	# make pre
	# Test that crashes table exists
	python3 ./test_db.py

task:
	# make task
	# Clean crashes data and insert into crashes table
	python3 ./task.py

post:
	# make post
	# Confirm crashes table has rows
	python3 ./post.py