

[
    ["test1", [
        ["key1", "value1"], 
        ["key2", "value2"],
    ]], 
    ["test2", [
        ["key3", "value3"],
    ]]
]

'''
test1
[['key1', 'value1'], ['key2', 'value2']]
test2
[['key3', 'value3'], ['key4', 'value4']]
'''
{
    "test1": {
        "key1": "value1",
        "key2": "value2"
    },
    "test2": {
        "key3": "value3"    
    }        
}



# for items, ((k1, v1), (k2, v2)) in L:
    # print(k1)
    # key1
    # key3
    # print(v1)
    # value1
    # value3
    # print(k2)    
    # key2
    # key4
    # print(v2)
    # value2
    # value4
# for items, (k, v) in L:
    # print(v)              
    # ['key2', 'value2']
    # ['key4', 'value4']
    # print(k)              
    # ['key1', 'value1']
    # ['key3', 'value3']
    # print(items)          
    # test1
    # test2
    
# for keys, values in L:
    # print({values[0][0] :values [0][0]})
    # test1
    # test2    
    # print(values)          
    # [['key1', 'value1'], ['key2', 'value2']]
    # [['key3', 'value3'], ['key4', 'value4']]


    
    


    # for item in values:
        # print(item[0], item[1])
        # key1 value1
        # key2 value2
        # key3 value3

        # print(item)
        # ['key1', 'value1']
        # ['key2', 'value2']
        # ['key3', 'value3']
        # ['key4', 'value4']

    # print(keys)
    # test1
    # test2    
    # print(values)          
    # [['key1', 'value1'], ['key2', 'value2']]
    # [['key3', 'value3'], ['key4', 'value4']]      
                                    
        
# for items in L:
    # print(items)            
    # ['test1', [['key1', 'value1'], ['key2', 'value2']]]
    # ['test2', [['key3', 'value3'], ['key4', 'value4']]]
    

# for items in L:          
    # for i in items:
        # print(i)               
        # test1
        # [['key1', 'value1'], ['key2', 'value2']]
        # test2
        # [['key3', 'value3'], ['key4', 'value4']]
        
# for items in L:
    # for item in items: 
        # for i in item:
            # print(i)            
            # t
            # e
            # s
            # t
            # 1
            # ['key1', 'value1']
            # ['key2', 'value2']
            # t
            # e
            # s
            # t
            # 2
            # ['key3', 'value3']
            # ['key4', 'value4']
