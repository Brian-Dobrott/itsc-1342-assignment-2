# [Brian Dobrott] - Assignment 2


def evaluate_packet(port, packet_size_bytes):

# I accidentally made this 440 the first time around
# This one checks ports
    if port == 80 or port == 443:
        return "STANDARD_WEB_TRAFFIC"        

# I called 'em PACKAGE instead of PACKET
# This one checks for unusually large packets
    elif packet_size_bytes > 1500:
        return "SUSPICIOUS_LARGE_PACKET"

# This one checks for unusually small packets
    elif packet_size_bytes < 64:
        return "SUSPICIOUS_SMALL_PACKET"

# Anything inbetween is considered clean and let through
    else:
        return "NORMAL_INTERNAL_TRAFFIC"