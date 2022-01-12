#!/bin/bash

# ------------------------------------------------------------------------------
# Create new user

read -p "...enter firstname > " firstname
read -p "...enter lastname > " lastname

username=${firstname:0:1}${lastname:2:1};

sudo useradd $username;
echo "...username ${username} created!";

# ------------------------------------------------------------------------------
# Comment Name and Surname is this script
currentFile=${0};
echo "# ${firstname} ${lastname}" >> $currentFile;

# ------------------------------------------------------------------------------
# Set Password for new user
sudo passwd $username;

# ------------------------------------------------------------------------------

# Expired password after 10 days (ask to change password on day 9)
sudo passwd -x 10 -w 9 $username;

# ------------------------------------------------------------------------------
