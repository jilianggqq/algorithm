#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List

# refer docs: https://www.liaoxuefeng.com/wiki/1016959663602400/1017496031185408
# https://www.liaoxuefeng.com/wiki/1016959663602400/1017496679217440


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        res, count = 0, 0
        sp, ep = 0, 0
        # 不需要-1，是<，不是<=
        while sp < len(intervals):
            if start[sp] >= end[ep]:
                count -= 1
                ep += 1
            else:
                count += 1
                sp += 1
            res = max(res, count)

        return res


if __name__ == '__main__':
    intervals = []
    intervals.append(Interval(0, 30))
    intervals.append(Interval(5, 10))
    intervals.append(Interval(15, 12))

    s = Solution()
    min = s.minMeetingRooms(intervals)
    print(min)

    # clear intervals, test again
    intervals.clear()
    intervals = [Interval(7, 10), Interval(2, 4)]
    min = s.minMeetingRooms(intervals)
    print(min)
