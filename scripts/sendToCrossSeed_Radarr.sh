#!/bin/bash

release_hash=$radarr_download_id
if [[ ${radarr_eventtype^^} == "TEST" ]]; then
	release_hash="Test Movie Release"
fi

curl -XPOST ${CROSS_SEED_HOST}/api/webhook?apikey=${CROSS_SEED_API} \
  -H 'Content-Type: application/json' \
  --data '{"infoHash":"'"${release_hash}"'"}'

exit 0