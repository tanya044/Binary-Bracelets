def strToBinary(s): 
    bin_conv = [] 
  
    for c in s: 
          
        # convert each char to 
        # ASCII value 
        ascii_val = ord(c) 
          
        # Convert ASCII value to binary 
        binary_val = bin(ascii_val) 
        bin_conv.append(binary_val[2:]) 
          
    return (' '.join(bin_conv)) 
  
# Driver Code 
if __name__ == '__main__': 
    s = 'MLH_TANYA_MLH'
  
print (strToBinary(s)) 
