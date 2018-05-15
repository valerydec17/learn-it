#!/bin/bash

if [ "$1" == "-h" ]; then
  echo "Usage: `basename $0` 'Movie name' 'Movie year' 'your rate' 
	Example:	./movie.sh 'Davil wears Prada' 2006 4 
	Output is written to movie.db file"
  exit 0
fi

echo $1,	$2,	$3,	$(date +%Y-%m-%d) >> movie.db	 
