# [Brian Dobrott] - Assignment 2 Unit Tests
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'code')))
from solution import evaluate_packet

# Test 1: Standard web port 80
assert evaluate_packet(80, 500) == "STANDARD_WEB_TRAFFIC", "Failed standard web port 80 check"

# Test 2: Standard web secure port 443
assert evaluate_packet(443, 2000) == "STANDARD_WEB_TRAFFIC", "Failed standard web port 443 check"

# Test 3: Non-standard port with oversized packet (> 1500 bytes)
assert evaluate_packet(22, 1600) == "SUSPICIOUS_LARGE_PACKET", "Failed oversized packet check"

# Test 4: Non-standard port with undersized packet (< 64 bytes)
assert evaluate_packet(3389, 40) == "SUSPICIOUS_SMALL_PACKET", "Failed undersized packet check"

# Test 5: Non-standard port with normal packet size
assert evaluate_packet(8080, 512) == "NORMAL_INTERNAL_TRAFFIC", "Failed normal traffic check"

print("ALL UNIT TESTS PASSED - ASSIGNMENT 2")