
def main():
    nums1 = [0, 0, 0, 0, 0, 0]
    nums2 = [-1, -2, 1, 2]
    m = 0
    n = 4
    total_num = m + n
    if n == 0:
        nums1 = nums1[:total_num]
    elif m == 0:
        nums1 = nums2[:total_num]
    else:
        for i in range(n):
            if nums2[i] >= nums1[m-1]:
                last = m
                for k in range(i, n):
                    nums1.insert(last, nums2[k])
                    last += 1
                break
            else:
                for j in range(m):
                    if nums1[j] > nums2[i]:
                        nums1.insert(j, nums2[i])
                        m += 1
                        break
    nums1 = nums1[:total_num]
    print(nums1)
    return 0

if __name__ == "__main__":
    main()