# aws_snapshots.py
# Author - Bharat Puri
#
# Every time this script is executed, it creates a snapshot of the given
# volume. It then checks number of snapshots available for
# the given volume. If the total number of snapshots exceed
# value of 'keep', then it deletes the older snapshots. It ensures
# that 'keep' number of newest snapshots are preserved.
#
# If you specify 0 as keep value, it will delete all the snapshots including
# the one it just created. Thus this script can be used to delete all the snapshots.
#
# Please use this script at your own risk. Although this code has been
# tested in production, I will not be liable for any damage it causes.

from boto.ec2.connection import EC2Connection
from datetime import datetime
import sys

# Substitute your access key and secret key here
aws_access_key = 'MY_ACCESS_KEY_HERE'
aws_secret_key = 'MY_SECRET_KEY_HERE'

if len(sys.argv) < 3:
    print "Usage: python manage_snapshots.py volume_id number_of_snapshots_to_keep description"
    print "volume id and number of snapshots to keep are required. description is optional"
    sys.exit(1)


vol_id = sys.argv[1]
keep = int(sys.argv[2])


conn = EC2Connection(aws_access_key, aws_secret_key)

volumes = conn.get_all_volumes([vol_id])
volume = volumes[0]
description = 'Created by manage_snapshots.py at ' + datetime.today().isoformat(' ')

if len(sys.argv) > 3:
    description = sys.argv[3]

if volume.create_snapshot(description):
    print 'Snapshot created with description: ' + description

snapshots = volume.snapshots()
snapshot = snapshots[0]

def date_compare(snap1, snap2):
    if snap1.start_time < snap2.start_time:
        return -1
    elif snap1.start_time == snap2.start_time:
        return 0
    return 1

snapshots.sort(date_compare)
delta = len(snapshots) - keep
for i in range(delta):
    print 'Deleting snapshot ' + snapshots[i].description
    snapshots[i].delete()
