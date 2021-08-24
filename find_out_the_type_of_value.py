import re
import requests
import json


def find_smth_in_dict(d, find_):
    return re.findall(find_, str(d))

def myprint(d):
    for k, v in d.items():
        if type(v) == dict:
            myprint(v)
        elif type(v) == list:
            for l in list(v):
                if type(l) == dict:
                    myprint(l)
        else:
            if k == key_name and v == key_value:
                print("{0} : {1}".format(k, v))



key_name = 'res'
key_value = 'ok'

d={}
response=requests.get("https://6117d75e30022f0017a05ff1.mockapi.io/api/v1/Dict1")
d0 = json.loads(response.text)

if type(d0)==list:
    len_d0=d0.__len__()
    print(len_d0)
    for x in range(len_d0):
        d=dict(d0[x])
else: d=d0

find_=r'\'res\': \'ok\''
print(find_)
is_key_value_in_dict=find_smth_in_dict(d,find_)
len_result_find = is_key_value_in_dict.__len__()
print('"Элемент \'', key_name, '\':\'', key_value, '\' встречается  ', len_result_find, ' раз/а')
#print(d)
myprint(d)


# 1.Объявление входящих данных
# data3 = """
#      {
#   "name1": "abc",
#   "name2": "dfg",
#   "res": "ok",
#   "name3": "sfd",
#   "name4": [
#     {
#       "name4.1.": "poi"
#     },
#     {
#       "name4.1.1": "poi",
#       "res": "ok"
#     }
#   ],
#   "name5": {
#     "res":"ok",
#     "name6": [
#       {
#         "res": "ok",
#         "name8": {
#           "res": "ok"
#         }
#       }
#     ]
#   }
# }
# """


# # 3 Функция поиска пути к искомым элементам
# i = 0
# z = 0
#
#
# # 4.1. - функция поиска элемента в дикте
# def pars_dict(dict_, key_name, key_value, placement):
#     type_resp = type(dict_)
#     if type_resp == dict:
#         len_dict = len(dict_)
#         dict_keys = list(dict_.keys())
#         i = 0
#         find_ = ''
#         while i < len_dict:
#             obj_name = dict_keys[i]
#             obj_value = response.get(obj_name)
#             type_obj = type(obj_value)
#             len_obj = len(obj_value)
#             if obj_name == key_name and obj_value == key_value:
#                 'there is "res":"ok" in ' + placement + '[' + key_name + ']'
#
#                 return [obj_value, i, key_name]
#
#             i += 1
#
#     return [obj_value, find_]
#
#
# def pars_list(response, key_value, key_name, placement):
#     new_dict = {}
#     i = 0
#     len_resp = response.__len__()
#     while i < len_resp:
#         new_dict = dict(response[i])
#
#         i += 1
#     response = new_dict
#
#     return response
#


#
# # 5 parsing data3
# z = 0
#
# while z < len_resp_total:
#     name = list(response_total)[z]
#     response = response_total.get(name)
#     if type(response) == str:
#         if name == key_name and response == key_value:
#             print('there is "res":"ok" in data3[', z, ']')
#     elif type(response) == dict:
#         placement = 'data3[' + str(z) + ']'
#         find_ = pars_dict(response, key_name, key_value, placement)[1]
#         print('there is "res":"ok" in ', placement, '[' + key_name + ']')
#     elif type(response) == list:
#         placement = 'data3[' + str(z) + ']'
#         response = pars_list(response, key_value, key_name, placement)
#         i = pars_dict(response, key_name, key_value, placement)[1]
#         print('there is "res":"ok" in ', placement, '[', i, '][', key_name, ']')
#     z += 1
