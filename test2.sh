#!/bin/ksh
print "Content-type: text/plain\r\n\r"
print "my query string from (GET) is \"$QUERY_STRING\""
print "\nmy stdin (from POST) is"
cat