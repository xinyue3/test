# a = b'233423423'
#
#
#
# import json
#
# x = json.loads(a.decode())
# print(x)



a = """
b'eyJhbGciOiJIUzUxMiIsImlhdCI6MTU4NTkxODgzOCwiZXhwIjoxNTg1OTIyNDM4fQ.eyJpZCI6MTl9.42dOfCkrgUjPAA2uUAjnb5EvEVTyD7C7qPz1E8O2_skJ4DpuNrmBI
IxDFbo79-eT-qLE-njQb4kzsLrvfxECGg'
"""
print(type(a))
if a.find("'"):
    if a[a.find("'") - 1] == 'b':
        x = a[a.find("'") + 1: -2]
        print(x)