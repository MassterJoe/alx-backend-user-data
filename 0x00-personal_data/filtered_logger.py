#!/usr/bin/env python3
""" Write a function called filter_datum
that returns the log message obfuscated"""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """filter_datum function """
    return re.sub(r'({0})[^{1}]*(?={1})'.format(
        '|'.join(map(re.escape, fields)), re.escape(separator)
        ), r'\1' + redaction, message)
