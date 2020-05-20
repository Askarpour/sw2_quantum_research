import json
import sys
with open(sys.argv[1], 'r') as f:
    a = json.load(f)
    print(a)