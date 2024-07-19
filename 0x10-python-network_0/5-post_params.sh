#!/bin/bash
# takes in URL, sends POST request to passed URL, & displays body of response, variable email must be sent with value test@gmail.com, variable subject must be sent with value I will always be here for PLD
 curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
