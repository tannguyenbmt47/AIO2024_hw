"""
Cho một list các số nguyên num_list và một sliding window có kích thước size k di
chuyển từ trái sang phải. Mỗi lần dịch chuyển 1 vị trí sang phải có thể nhìn thấy
đươc k số trong num_list và tìm số lớn nhất trong k số này sau mỗi lần trượt k phải
lớn hơn hoặc bằng 1
Input: num_list = [3, 4, 5, 1, -44 , 5 ,10, 12 ,33, 1] với k=3
Output: [5, 5, 5, 5, 10, 12, 33, 33]
"""

def find_max_sliding_window(num_list: list[int], k: int):
    result = []
    
    for i in range(len(num_list) - k + 1):
        window = []
        for j in range(k):
            window.append(num_list[i+j])

        result.append(max(window))
    
    return result

if __name__ == "__main__":
    num_list = [3, 4, 5, 1, -44 , 5 ,10, 12 ,33, 1]
    k = 3

    result = find_max_sliding_window(num_list, k)
    print(result)