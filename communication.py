import random   # Used to generate random numbers (to simulate packet loss)
import time     # Used to add delay between packet transmissions

packet_count = 5        # Total number of packets to send
loss_probability = 0.3  # 30% chance that a packet will be lost

# Loop through each packet
for packet in range(1, packet_count + 1):

    delivered = False   # Initially assume the packet is not delivered

    # Keep sending the packet until it is successfully delivered
    while not delivered:
        print(f"Sending packet {packet}...")
        
        time.sleep(1)   # Pause for 1 second to simulate transmission delay

        # random.random() generates a number between 0 and 1
        # If the number is less than 0.3, we simulate packet loss
        if random.random() < loss_probability:
            print("Packet lost! Retrying...")
        
        else:
            # Packet successfully received
            print("Packet received!")
            delivered = True   # Exit the loop once delivery is successful