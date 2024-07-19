#!/bin/bash
# makes request to 0.0.0.0:5000/catch_me which makes the server respond with "You got me!", in body of response.
curl -s -L -X PUT -d user_id=98 -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me
