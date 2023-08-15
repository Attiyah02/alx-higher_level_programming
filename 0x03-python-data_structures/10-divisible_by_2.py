#!/usr/bin/python3
def divisible_by_2(m_list=[]):
    new_list = []
    for m in range(len(m_list)):
        if m_list[m] % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return new_list
