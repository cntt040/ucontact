#!/usr/bin/env python

import nose
import os

args = ['tests', '--with-spec', '--spec-color', '--nologcapture', '--no-byte-compile']

nose.run(argv=args)

