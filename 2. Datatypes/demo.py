def count_substring(string, sub_string):
    count = 0
    length_of_substring = len(sub_string)
    #print(length_of_substring)
    for index in range(len(string)):
        print(index)
    # for index in range[len(string)]:
    #     if(index + length_of_substring > len(string)):
    #         break
    #     print(string[index:index+length_of_substring])
    #     if(string[index:index+length_of_substring] == sub_string):
    #         count += 1

    return count

if __name__ == '__main__':
    string = "ADCDCDC"
    sub_string = "CDC"
    
    count = count_substring(string, sub_string)
    print(count)