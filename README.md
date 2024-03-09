# Text encryption

In a flight, want to try creating my own text compressor and uncompressor

- [ ] Gather a large corpus. 
- [ ] Break it down into samples of various sizes 
- [ ] Track time of compressing and uncompressing
- [ ] Track size 

## Size analysis

```python
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
```

*output*
```python
Number of lines: 13169
Total: 2043690 bytes
On average each line contains: 155.18946009567924 bytes
```




## Benchmark
Original size of `text-file.input`: `1.1 mb` 

### Just using pickle
`text-file-full-size.simple_enc_with_pickle`: `1.1 mb`

Compression took 0.023513041000000002 seconds

### Bimap and using pickle
- Create a bimap where each word maps to a value and vice versa
- Encoding
  - output two things: (1) the bimap (2) encoded text


Final size: `text-file-full-size.compress_bimap` -> 3 MB (even with `pickle.HIGHEST_PROTOCOL`)
Final size: `text-file-full-size.bimap` -> 1 KB
```python
ENCODING USING BIMAP
Compression took 0.025853917000000004 seconds

```

```python
DECODING USING BIMAP
Action took 0.17835133399999997 seconds
```

### Bimap and using custom serializer
- Similar as the previous step except serializes using `ListSerializer`

Fina size: `text-file-full-size.compress_bimap_custom` -> 2.9 mb
Final size: `text-file-full-size.bimap_custom` -> 1 KB (same logic as previous)

```python
ENCODING USING BIMAP AND CUSTOM SERIALIZER
Action took 0.266223334 seconds
DECODING USING BIMAP AND CUSTOM SERIALIZER
Action took 0.177122375 seconds
```