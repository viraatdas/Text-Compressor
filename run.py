import pickle
import sys
import timeit
from util.BiDirectionalMap import BiDirectionalMap
from util.ListSerializer import dump, load

def simple_compress_with_pickle(file):
    with open(file, "r") as read_file:
        text = read_file.readlines()

    with open(file + ".compress_pickle", "wb") as pickle_output:
        pickle.dump(text, pickle_output)        


def size_analysis(file):
    total_number_of_bytes = 0
    num_elements = 0
    with open(file, "r") as f:
        text = f.readlines()
        for el in text:
            total_number_of_bytes += sys.getsizeof(el)
            num_elements+=1
    print(f"Number of lines: {num_elements}")
    print(f"Total: {total_number_of_bytes} bytes")
    print(f"On average each line contains: {total_number_of_bytes/num_elements} bytes")

# method returns two output:
# (1) a BiDirectional map with the values of the word
# (2) the compressed form of the word
def compress_bimap_pickle(file):
    bi_map = BiDirectionalMap()
    output = []
    with open(file, "r") as f:
        text = f.readlines()
        for line in text:
            for word in line:
                bi_map.put(word)    
        
        for line in text:
            curr_line = ""
            for word in line:
                curr_line += str(bi_map.get_value(word)) + " "
            output.append(curr_line)
    
    # print(output)
    with open(file+".compress_bimap_pickle", "wb") as f:
        pickle.dump(output, f, protocol=pickle.HIGHEST_PROTOCOL)
    with open (file +".bimap_pickle", "wb") as f:
        pickle.dump(bi_map, f)
    

def decompress_bimap_pickle(encoded_file, bi_map_file):

    bi_map = None
    encoded_text = None
    with open(bi_map_file, "rb") as f:
        bi_map = pickle.load(f)
    
    with open(encoded_file, "rb") as f:
        encoded_text = pickle.load(f)

    output = []
    for line in encoded_text:
        curr_line = ""
        for value in line.split():
            curr_line += bi_map.get_word(int(value))
        output.append(curr_line)
    # print(output)

def compress_bimap_custom(file):
    bi_map = BiDirectionalMap()
    output = []
    with open(file, "r") as f:
        text = f.readlines()
        for line in text:
            for word in line:
                bi_map.put(word)    
        
        for line in text:
            curr_line = ""
            for word in line:
                curr_line += str(bi_map.get_value(word)) + " "
            output.append(curr_line)
    
    dump(output, file+".compress_bimap_custom")
    with open (file +".bimap_custom", "wb") as f:
        pickle.dump(bi_map, f)
    

def decompress_bimap_custom(encoded_file, bi_map_file):

    bi_map = None
    encoded_text = None
    with open(bi_map_file, "rb") as f:
        bi_map = pickle.load(f)
    
    encoded_text = load(encoded_file)

    output = []
    for line in encoded_text:
        curr_line = ""
        for value in line.split():
            curr_line += bi_map.get_word(int(value))
        output.append(curr_line)
    # print(output)





### Utility methods
def time_method(lambda_expression, num_times=5):
    time = timeit.timeit(lambda_expression, number=num_times) 
    print(f"Action took {time} seconds")



file = "text-file-full-size"


### Encoding and decoding using just pickle
# time_method(lambda: simple_compress_with_pickle(file))


#### Encoding and decoding using bimap and pickle method
# print("ENCODING USING BIMAP AND PICKLE")
# time_method(lambda: compress_bimap_pickle(file), num_times=1)

# bi_map_file = "text-file-full-size.bimap"
# encoded_bimap_file = "text-file-full-size.compress_bimap"
# print("DECODING USING BIMAP AND PICKLE")
# time_method(lambda: decompress_bimap_pickle(encoded_bimap_file, bi_map_file), num_times=1)


#### Encoding and decoding using bimap and custom serializer method

print("ENCODING USING BIMAP AND CUSTOM SERIALIZER")
time_method(lambda: compress_bimap_custom(file), num_times=1)

bi_map_custom_file = "text-file-full-size.bimap_custom"
encoded_bimap_custom_file = "text-file-full-size.compress_bimap_custom"
print("DECODING USING BIMAP AND CUSTOM SERIALIZER")
time_method(lambda: decompress_bimap_custom(encoded_bimap_custom_file, bi_map_custom_file), num_times=1)

