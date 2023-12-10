import polars as pl
import re

#problem Url:https://adventofcode.com/2023/day/1

#Part:1
sum_1 = pl.read_csv(r'E:\Advent of Code 2023\AOC-2023\day_1\day_1_input.txt',
                 has_header=False)\
        .with_columns(pl.col('column_1').str.extract_all(r'\d')\
        .map_elements(lambda x:int("".join([x[0],
                                            x[-1]]))).alias('2_digits_sum'))\
        .select(pl.col('2_digits_sum').sum())
print(sum_1)


#part:2
def get_list_of_digits(input):

    import re

    word_to_digit = {
    "one": "1", "two": "2", "three": "3",
    "four": "4", "five": "5", "six": "6",
    "seven": "7", "eight": "8", "nine": "9",
    }

    digit_index_dict = {}

    for word, digit in word_to_digit.items():
        
        match_wd_lst = list(re.finditer(word,input))
        if match_wd_lst:
            for wd in match_wd_lst:
                digit_index_dict[wd.start()] = digit
        
        match_dig_lst = list(re.finditer(digit,input))
        if match_dig_lst:
            for dig in match_dig_lst:
                digit_index_dict[dig.start()] = digit

    sorted_dict = dict(sorted(digit_index_dict.items()))
    
    sorted_values = list(sorted_dict.values())
    
    return sorted_values
    

sum_2 = pl.read_csv(r'E:\Advent of Code 2023\AOC-2023\day_1\day_1_input.txt',
                 has_header=False)\
                .with_columns(pl.col('column_1').\
                    map_elements(lambda x:get_list_of_digits(x)).alias('word_to_digits'))\
                .with_columns(pl.col('word_to_digits')\
                .map_elements(lambda x:int("".join([x[0],
                                                    x[-1]]))).alias('2_digits_sum'))\
                .select(pl.col('2_digits_sum').sum())
                                          
                
                              
print(sum_2)