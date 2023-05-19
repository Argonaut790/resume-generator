import heapq
from collections import OrderedDict

test_dict = {('PJ_NAME', 0): '', ('PJ_START_MON', 0): 'Jan', ('PJ_START_YEAR', 0): '', 
          ('PJ_END_MON', 0): 'Jan', ('PJ_END_YEAR', 0): '', ('PJ_START', 0): 'Jan 2023', 
          ('PJ_END', 0): 'Jan 2023', ('PJ_LIST', 0, 0): '123', ('PJ_LIST', 0, 1): '456', 
          ('PJ_NAME', 1): '', ('PJ_START_MON', 1): 'Jan', ('PJ_START_YEAR', 1): '', 
          ('PJ_END_MON', 1): 'Jan', ('PJ_END_YEAR', 1): '', ('PJ_START', 1): 'Jan 2023', 
          ('PJ_END', 1): 'Jan 2023', ('PJ_LIST', 1, 0): '', ('PJ_LIST', 0, 2): '789'}

temp_list = [(k, v) for k, v in test_dict.items()]
heapq.heapify(temp_list)
res = dict(heapq.heappop(temp_list) for i in range(len(temp_list)))

print("KEYS:")
print(test_dict.items())
print("SORTED:")
print(sorted(test_dict.items(), key=lambda key: key[0][1]))