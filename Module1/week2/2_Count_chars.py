'''
Viết function trả về một dictionary đếm số lượng chữ xuất hiện trong một từ, với key là chữ cái
và value là số lần xuất hiện
• Input: một từ
• Output: dictionary đếm số lần các chữ xuất hiện
• Note: Giả sử các từ nhập vào đều có các chữ cái thuộc [a-z] hoặc [A-Z]
'''


def count_chars(string):
    result = {}
    for i in string:
        if i not in result.keys():
            result[i] = 1
        else:
            result[i] += 1

    print(result)


if __name__ == "__main__":
    string = 'Happiness'
    count_chars(string)

    string = 'smiles'
    count_chars(string)
