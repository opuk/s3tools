#!/bin/sh
#echo -n "Password: "
#read -s pwd
#export PASSPHRASE=$pwd

#GPG_KEY=[your-gpg-key]

# The source of your backup
SOURCE=$HOME

DEST=s3+http://$BUCKET/$HOSTNAME

#--verbosity 9 \
#    --asynchronous-upload \
#    --verbosity info \
duplicity \
    --volsize 25 \
    --full-if-older-than 1M \
    --progress \
    --s3-european-buckets \
    --s3-use-rrs \
    --s3-use-new-style \
    --exclude=**Downloads \
    --exclude=**.SpiderOak \
    --exclude=**.cache \
    --exclude=**iso \
    ${SOURCE} ${DEST}

