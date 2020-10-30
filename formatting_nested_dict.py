a = {
    "ambition": {
        "coat": {
            "ex": "fruit",
            "eblan": "four",
            "extreme": "forecast"
        },
        "corruption": {
        },
        "claim": "driver"
    },
    "adjust": {
        "crossing": "dress",
        "crutch": "dinner"
    },
    "automatic": "banish"
}




def format_nested(nested_dict):
    def pretty_print(nested_dict, indent):
        tab_indent = '\t' * indent
        for i, (key, value) in enumerate(nested_dict.items()):

            if isinstance(value, dict):
                print('{0}"{1}": {{'.format(tab_indent, str(key)))
                pretty_print(value, indent+1)

                if i == len(nested_dict)-1:
                    print('{0}}}'.format(tab_indent))
                else:
                    print('{0}}},'.format(tab_indent))
            else:
                line = '{0}"{1}": "{2}"'.format(tab_indent, str(key), value)
                if i != len(nested_dict)-1:
                    line = f'{line},'
                print(line)
    print('{')
    pretty_print(nested_dict,indent=1)
    print('}')


print(format_nested(a))
