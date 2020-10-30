def longest_common_substr(first_str, second_str):
    length_first = len(first_str) 
    length_second = len(second_str)  

    counter_suffix = [[0 for k in range(length_second+1)] for l in range(length_first+1)]    
    longest_line = 0

    for i in range(length_first):
        for j in range(length_second):
            if first_str[i] == second_str[j]:
                counter = counter_suffix[i][j] + 1
                counter_suffix[i+1][j+1] = counter
                if counter > longest_line:
                    longest_common_substr_list = list()
                    longest_line = counter
                    longest_common_substr_list.append(first_str[i-counter+1:i+1])
                elif counter == longest_line:
                    longest_common_substr_list.append(first_str[i-counter+1:i+1])

    return longest_common_substr_list
      
    
first_str = 'abab'
second_str = 'baba'
  
print(longest_common_substr(first_str, second_str)) 
  
