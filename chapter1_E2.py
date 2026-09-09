



portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]

D = [
    [0,8943,8019,3652,10545],
    [8943,0,2619,6317,2078],
    [8019,2619,0,5836,4939],
    [3652,6317,5836,0,7825],
    [10545,2078,4939,7825,0]
]

co2 = 0.020

# Initialize global tracking variables
smallest = 1000000
bestroute = []

def permutations(route, ports):
    # Origin of scope resolution: Explicitly request write access to global memory
    global smallest, bestroute

    # Base case: execute evaluation when the permutation is complete
    if len(ports) == 0:
        # Corrected memory lookup using the matrix identifier 'D'
        distances = (D[route[0]][route[1]] +
                     D[route[1]][route[2]] +
                     D[route[2]][route[3]] +
                     D[route[3]][route[4]])
        
        emissions = distances * co2
        
        # Corrected attribute access: compare the primitive float directly
        if emissions < smallest:
            smallest = emissions
            bestroute = route
            
    # Recursive step
    else:
        for i in range(len(ports)):
            new_route = route + [ports[i]]
            new_ports = ports[:i] + ports[i+1:]
            permutations(new_route, new_ports)

def main():
    # Do not edit any (global) variables using this function, as it will mess up the testing
    # this will start the recursion
    permutations([0], list(range(1, len(portnames))))

    # print the best route and its emissions
    print(' '.join([portnames[i] for i in bestroute]) + " %.1f kg" % smallest)

main()
