def count_pairs_with_sum(arr, K):
    count = 0
    num_frequency = {}  

    for number in arr:
        complement = K - number  
        
        # if sum exists then 
        if complement in num_frequency:
            count += num_frequency[complement]  

        # update no. of pairs found
        if number in num_frequency:
            num_frequency[number] += 1
        else:
            num_frequency[number] = 1

    return count

def main():
   
    arr = [1,2,3,4]
    K = 6
    
    result = count_pairs_with_sum(arr, K)
    
    print(f"total pairs with sum {K}: {result}")

# execute main
if __name__ == "__main__":
    main()