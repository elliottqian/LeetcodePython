# -*- coding: utf-8 -*-

"""
快速排序

快速排序还可以迅速找到中位数
"""

test_list = [3, 2, 6, 4, 1, 8, 0, 2]


def quick_sort(num_list, left, right):
	l = left
	r = right
	if left >= right:
		return
	standard = num_list[l]
	empty_index = l
	move_right = True
	while(l < r):
		if move_right:
			if num_list[r] < standard:
				num_list[empty_index] = num_list[r]
				empty_index = r
				move_right = False
			else:
				r -= 1
		else:
			if num_list[l] > standard:
				num_list[empty_index] = num_list[l]
				empty_index = l
				move_right = True
			else:
				l += 1
	num_list[empty_index] = standard
	print(test_list)


	print(left, empty_index)
	quick_sort(num_list, left, empty_index - 1)
	print(empty_index, right)
	quick_sort(num_list,  empty_index + 1, right)
	pass


if __name__ == "__main__":

	quick_sort(test_list, 0, len(test_list) - 1)
	print(test_list)
	pass