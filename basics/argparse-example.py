#!/bin/python3
import argparse

parser = argparse.ArgumentParser(prog="Argument Parser example", description="This is a more detailed description")
parser.add_argument("-n", "--name", required=True, help="Enter first name")
parser.add_argument("-s", "--surname", required=False, help="Enter the last name")
args = parser.parse_args()

print("My name is {} {}".format(args.name, str(args.surname or '')))
