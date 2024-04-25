#!/bin/bash

w=pneumonoultramicroscopicsilicovolcanoconiosis

grep -o "o" <<<"$w" | wc -l
