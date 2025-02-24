# Inefficient: Retaining large unused lists

def inefficient_list():
    large_list = [i for i in range(10 ** 6)]  # Large list

    print("List created")

    # The function retains memory until it ends


inefficient_list()


# Efficient: Explicitly releasing memory

def efficient_list():
    import gc  # Garbage collection module

    large_list = [i for i in range(10 ** 6)]

    print("List created")

    del large_list  # Remove reference to list

    gc.collect()  # Force garbage collection


efficient_list() 