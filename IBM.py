# #!/bin/python3

# # Complete the 'getMinimumCost' function below.
# #
# # The function is expected to return a LONG_INTEGER.
# # The function accepts following parameters:
# # 1. INTEGER edgeDeviceCost
# # 2. INTEGER inputPeripheralCost
# # 3. INTEGER bundleCost
# # 4. INTEGER x
# # 5. INTEGER y
# #

# def getMinimumCost(edgeDeviceCost, inputPeripheralCost, bundleCost, x, y):
#     # Calculate the effective cost of buying a bundle instead of individual items
#     effectiveBundleCost = min(bundleCost, edgeDeviceCost + inputPeripheralCost)

#     # Initialize minimum cost
#     minCost = float('inf')

#     # Iterate through possible number of bundles to purchase
#     for bundles in range(max(x, y) + 1):
#         # Devices and peripherals left after purchasing bundles
#         remainingEdgeDevices = max(0, x - bundles)
#         remainingPeripherals = max(0, y - bundles)

#         # Cost of the current configuration
#         currentCost = (bundles * effectiveBundleCost) + \
#                       (remainingEdgeDevices * edgeDeviceCost) + \
#                       (remainingPeripherals * inputPeripheralCost)

#         # Update minimum cost if current configuration is cheaper
#         minCost = min(minCost, currentCost)

#     return minCost

# if __name__ == '_main_':
#     edgeDeviceCost = int(input().strip())
#     inputPeripheralCost = int(input().strip())
#     bundleCost = int(input().strip())
#     x = int(input().strip())
#     y = int(input().strip())

#     result = getMinimumCost(edgeDeviceCost, inputPeripheralCost, bundleCost, x, y)

# print(result)






def getNumberOfDroppedPackets(requests, max_packets, rate):
    # Initialize variables
    current_time = 0
    pipeline = 0
    dropped_packets = 0
    
    # Sort requests by time (optional but ensures correct order if unsorted)
    requests.sort(key=lambda x: x[0])
    
    for request in requests:
        request_time, packets = request
        
        # Update pipeline based on the time elapsed
        if request_time > current_time:
            # Calculate packets delivered during the elapsed time
            time_elapsed = request_time - current_time
            pipeline = max(0, pipeline - time_elapsed * rate)
            current_time = request_time
        
        # Add new packets to the pipeline
        pipeline += packets
        
        # Check if the pipeline exceeds max capacity
        if pipeline > max_packets:
            dropped_packets += pipeline - max_packets
            pipeline = max_packets
    
    return dropped_packets


if __name__ == '_main_':
    # Sample input for testing
    requests = [[2, 8], [1, 10], [3, 4]]
    max_packets = 7
    rate = 5

    result = getNumberOfDroppedPackets(requests, max_packets, rate)
    print(result)  # Expected output: 6