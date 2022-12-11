#!/usr/bin/python
# -*- coding: utf-8 -*-
import os


def test_hello2():
    return "Hello World2"


if __name__ == "__main__":
    print(test_hello2())
    print(os.environ.get('TEST_KEY'))
