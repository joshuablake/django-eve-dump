#!/usr/bin/env bash
USER=root
DATABASE=wspacekills
cd /tmp
wget https://www.fuzzwork.co.uk/dump/mysql-latest.tar.bz2
sql=$(tar xvjf mysql-latest.tar.bz2 | grep sql)
mysql -u$USER -D$DATABASE < $sql
