# Uses python3
from operator import itemgetter

def optimal_points(segments):
    points = []
    sorted_segments = sorted(segments, key = itemgetter(1))
    cur_segment = sorted_segments.pop(0)
    cur_point = cur_segment[1]
    points.append(cur_point)
    while True:
    	if (cur_point >= sorted_segments[0][0]) and (cur_point <= sorted_segments[0][1]):
    		sorted_segments.pop(0)
    	else:
    		cur_segment = sorted_segments.pop(0)
    		cur_point = cur_segment[1]
    		points.append(cur_point)
    	if len(sorted_segments) == 0:
    		return points

if __name__ == '__main__':
    n = int(input())
    segments = []
    for _ in range(n):
    	segment = list(map(int, input().split()))
    	segments.append(segment)
    points = optimal_points(segments)
    print(len(points))
    print(*points)
