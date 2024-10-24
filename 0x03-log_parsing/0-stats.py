#!/usr/bin/python3
'''A script for parsing HTTP request logs.
'''
import re


def extract(line):
    '''Extracts sections of a line from an HTTP request log.
    '''
    patterns = (
        r'\s*(?P<ip>\S+)\s*',
        r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',
        r'\s*"(?P<request>[^"]*)"\s*',
        r'\s*(?P<status>\S+)',
        r'\s*(?P<size>\d+)'
    )
    log_fmt = '{}\\-{}{}{}{}\\s*'.format(*patterns)
    match = re.fullmatch(log_fmt, line)
    if match:
        return {
            'status': match.group('status'),
            'size': int(match.group('size'))
        }
    return {}


def stats(size, codes):
    '''Prints the accumulated statistics.
    '''
    print(f'File size: {size}', flush=True)
    for code in sorted(codes.keys()):
        if codes[code] > 0:
            print(f'{code}: {codes[code]}', flush=True)


def update(line, size, codes):
    '''Updates metrics from a given log line.
    '''
    info = extract(line)
    if info and info['status'] in codes:
        codes[info['status']] += 1
    return size + info.get('size', 0)


def run():
    '''Starts the log parser.
    '''
    line_num = 0
    size = 0
    codes = {'200': 0, '301': 0, '400': 0, '401': 0,
             '403': 0, '404': 0, '405': 0, '500': 0}
    try:
        while True:
            line = input()
            size = update(line, size, codes)
            line_num += 1
            if line_num % 10 == 0:
                stats(size, codes)
    except (KeyboardInterrupt, EOFError):
        stats(size, codes)


if __name__ == '__main__':
    run()
