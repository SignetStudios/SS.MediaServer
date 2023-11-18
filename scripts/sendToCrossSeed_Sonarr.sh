#!/bin/bash

release_hash=$sonarr_download_id
if [[ ${sonarr_eventtype^^} == "TEST" ]]; then
	release_hash="Test TV Release"
fi

curl -XPOST ${CROSS_SEED_HOST}/api/webhook?apikey=${CROSS_SEED_API} \
  -H 'Content-Type: application/json' \
  --data '{"infoHash":"'"${release_hash}"'"}'

exit 0