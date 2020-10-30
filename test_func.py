
# put here 
# import <your_file_name> import <your_func_name> as array_to_dict 
from list_to_dict import convert as array_to_dict 

def test_description():
    arr = [
        ["test1", [
            ["key1", "value1"], 
            ["key2", "value2"],
        ]], 
        ["test2", [
            ["key3", "value3"],
        ]]
    ]
    real_dict = array_to_dict(arr)
    expect_dict = {
        "test1": {
            "key1": "value1",
            "key2": "value2"
        },
        "test2": {
            "key3": "value3"    
        }        
    }

    assert real_dict == expect_dict

def test_one_key():
    arr = [
        ["test1", [
            ["key1", "value1"], 
        ]]
    ]
    real_dict = array_to_dict(arr)
    expect_dict = {
        "test1": {
            "key1": "value1",
        }     
    }

    assert real_dict == expect_dict

def test_three_keys():
    arr = [
        ["test1", [
            ["key1", "value1"], 
            ["key3", "value3"],
        ]],
        ["test2", [
            ["key1", "value1"], 
        ]],
        ["test3", [
            ["key1", "value1"], 
            ["key4", "value1"], 
            ["key5", "value2"], 
        ]]
    ]
    real_dict = array_to_dict(arr)
    expect_dict = {
        "test1": {
            "key1": "value1",
            "key3": "value3"
        },
        "test2": {
            "key1": "value1", 
        },
        "test3": {
            "key1": "value1", 
            "key4": "value1", 
            "key5": "value2", 
        }
    }

    assert real_dict == expect_dict

def test_empty_keys():
    arr = [
        ["test1", [
        ]]
    ]
    real_dict = array_to_dict(arr)
    expect_dict = {
        "test1": {}
    }

    assert real_dict == expect_dict
