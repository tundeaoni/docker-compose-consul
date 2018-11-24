#! /bin/bash
psql  -U greeter -c "CREATE TABLE greeting ( message TEXT NOT NULL);"
psql  -U greeter -c "INSERT INTO greeting (message) VALUES ('Hello, world');"
