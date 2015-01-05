#!/bin/sh
# Export some ENV variables so you don't have to type anything
#echo -n "Password: "
#read -s pwd
#export PASSPHRASE=$pwd

#GPG_KEY=[your-gpg-key]

# The source of your backup
#SOURCE=/home/user

DEST=s3+http://$BUCKET/$HOSTNAME

#--verbosity 9 \
duplicity remove-all-but-n-full 1 --force ${DEST}

