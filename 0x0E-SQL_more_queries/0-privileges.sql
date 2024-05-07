#!/bin/bash

# MySQL credentials
MYSQL_USER="root"
MYSQL_PASSWORD="root"
MYSQL_HOST="localhost"

# Function to show grants for a user
show_user_grants() {
    local user="$1"
    mysql -u"$MYSQL_USER" -p"$MYSQL_PASSWORD" -h"$MYSQL_HOST" -e "SHOW GRANTS FOR '$user'@'$MYSQL_HOST';"
}

# List privileges for user_0d_1
echo "Privileges for user_0d_1:"
show_user_grants "user_0d_1"

# List privileges for user_0d_2
echo "Privileges for user_0d_2:"
show_user_grants "user_0d_2"
