
    
def get_aspect_ratio(resolution):
    '''
    Signature:  Tuple -> Tuple
    Purpose:    Produce a tuple that shows aspect ratio of an image from
                a given resolution of image using Euclid's algorithm to find Greatest
                Comman Divisor, recursion, and inner function
    Tests:      get_aspect_ratio((1920, 1080)) -> (16, 9)
    Stub:       def get_aspect_ratio(resolution): aspect_ratio
    '''
    # Conditions:
    # - Number of elements in tuple is 2
    # - Elements are integer
    # - No value is zero
    assert  len(resolution) == 2 and \
            tuple(map(int, resolution)) and \
            all(resolution) 


    def get_gcd(big_number, small_number):
        '''
        Signature:  Recursion | 2 Integers -> Integer
        Purpose:    Produce an integer that is the greatest common divisor of
                    2 given integers using Euclid's algorithm
        Tests:      N/A
        Stub:       def get_gcd(big_number, small_number)
        '''
        if big_number == small_number:
            return big_number # Return itself as the GCD
        elif big_number < small_number:
            return get_gcd(small_number, big_number)
            # big_number is smaller than small_number, return adjusted function

        if small_number == 0:
            return big_number
        else:
            return get_gcd(small_number, big_number % small_number)


    gcd = get_gcd(*resolution)  # Assign gcd using get_gcd()
    return tuple(number // gcd for number in resolution)  # Divide width, height by GCD

'''
Tests
'''
#resolution0 = (0, 0)
resolution1 = (1920, 1080)
resolution2 = (900, 1440)
resolution3 = (1000, 1000)

result = lambda resolution, aspect_ratio: f'Resolution {resolution[0]}x{resolution[1]} \
-> Aspect ratio {aspect_ratio[0]}:{aspect_ratio[1]}'

#print(result(resolution0, get_aspect_ratio(resolution0)))
print(result(resolution1, get_aspect_ratio(resolution1)))
print(result(resolution2, get_aspect_ratio(resolution2)))
print(result(resolution3, get_aspect_ratio(resolution3)))
