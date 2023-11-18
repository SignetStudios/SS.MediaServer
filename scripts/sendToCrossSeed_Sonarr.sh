#!/bin/bash

torrentHash="${sonarr_download_id}"

if [[ "${sonarr_eventtype}" == "Test" ]]; then
  torrentHash="Test Download Id"
fi

curl -XPOST http://cross-seed:2468/api/webhook \
  -H 'Content-Type: application/json' \
  --data "{'infoHash': '${torrentHash}'}"

