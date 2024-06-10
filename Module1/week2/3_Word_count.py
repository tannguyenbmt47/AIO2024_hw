'''
Viết function đọc các câu trong một file txt, đếm số lượng các từ xuất hiện và trả về một dictionary
với key là từ và value là số lần từ đó xuất hiện.
• Input: Đường dẫn đến file txt
• Output: dictionary đếm số lần các từ xuất hiện
• Note:
    - Giả sử các từ trong file txt đều có các chữ cái thuộc [a-z] hoặc [A-Z]
    - Không cần các thao tác xử lý string phức tạp nhưng cần xử lý các từ đều là viết
thường
    - Các bạn dùng lệnh này để download
!gdown https://drive.google.com/uc?id=1IBScGdW2xlNsc9v5zSAya548kNgiOrko
'''

def word_count(file_path):
    result = {}

    with open(file_path,"r") as f:
        data = f.read()
    new_data = data.replace("\n"," ").lower()

    for i in new_data.split(" "):
        if i not in result.keys():
            result[i] = 1
        else:
            result[i] += 1

    print(result)

if __name__ == "__main__":
    file_path = "data/P1_data.txt"

    word_count(file_path)