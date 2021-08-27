#!/bin/bash

function variable_in_string(){
	num=100
	echo "$num"
	echo ''$num''
	echo '$num'
}

variable_in_string
