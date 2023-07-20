#!/usr/bin/python3
"""
Task 0 Module - Script that parses server logs.
"""
import sys
import re

counter = 0
files = 0
codes_counter = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0
        }


def print_stats(codes_dict, total_files):
    """
    Prints out server requests statistics
    """
    print('File size: {}'.format(total_files))
    for key in sorted(codes_dict.keys()):
        if codes_dict[key] > 0:
            print('{}: {}'.format(key, codes_dict[key]))


if __name__ == '__main__':
    try:
        for line in sys.stdin:
            counter += 1

            line = re.split('- |"|"| " " ', line)
            if len(line) != 4:
                continue
            st_code_file_size = line[-1]

            try:
                st_code = int(st_code_file_size.split()[0])
                file_size = int(st_code_file_size.split()[1])

                if st_code in codes_counter:
                    codes_counter[st_code] += 1

                files += file_size
            except Exception:
                pass

            if counter % 10 == 0 and counter > 0:
                # print stats
                print_stats(codes_counter, files)
        print_stats(codes_counter, files)

    except KeyboardInterrupt:
        # print stats
        print_stats(codes_counter, files)
        raise
