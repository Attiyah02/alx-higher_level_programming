#!/usr/bin/python3
def max_integer(m_list=[]):
    if len(m_list) == 0:
        return "None"
    else:
        max = m_list[0]
        for m in range(len(m_list)):
            if m_list[m] > max:
                max = m_list[m]
        return max
