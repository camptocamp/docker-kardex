#!/usr/bin/python3
import os
import ssl
import sys
import time

from kardex_proxy import main, make_parser

parser = make_parser()
args = parser.parse_args()
main(args)
sys.exit(0)
