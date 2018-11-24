#! /bin/bash
echo "Table greeting"
psql  -U greeter -c "CREATE TABLE greeting ( message TEXT NOT NULL);"

echo "seed"
psql  -U greeter -c "INSERT INTO greeting (message) VALUES ('Hello, world');"
