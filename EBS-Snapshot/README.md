EBS Snapshots with Python Script

This script creates a new ebs snapshot and deletes all the previous snapshots except a few newest snapshots.

How to use this script

The script takes three arguments:

1) volume-id – This is Amazon’s volume id

2) number of snapshots to preserve – An integer. If you specify 2 it will keep 2 newest snapshots (including the one it just created). If you specify 0, the script will delete all the snapshots (including the one it just created).

3) description (optional) – Description you want to use for your snapshot.


Syntax

python aws_snaphots.py vol-dkls343e 2 'daily snapshot'



