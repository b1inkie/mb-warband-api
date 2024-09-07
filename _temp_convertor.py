import os,re,importlib.util,pyperclip

import _tools.utils as utils


# 正则去除所有非OP注释
# 正则去空行
def format_op():
    with open('op/tmp.py','r',encoding='utf-8') as f:
        data = f.read()

    res = {}
    count = 0
    for line in data.split('\n'):

        if line[0] != ' ': # 是操作号行
            count += 1
            if not res.get(count):
                res[count] = {}
            anly_line = re.findall(r"(.*?)\s.*?=\s.*?(\S.*?)\s.*?#.*?\((.*?)\)",line)

            res[count]['op'] = anly_line[0][0]
            res[count]['op_key'] = anly_line[0][1]
            res[count]['method'] = anly_line[0][2]
            res[count]['explain'] = ''
        else:
            anly_line = re.findall(r".*?#(.*)",line)
            res[count]['explain'] += '#' + anly_line[0]
            
    return res


def pack(op_dict):
    data = '{\n'
    for group in op_dict.values():
        _body = group.get('method').split(',')
        body = '('+f"{group.get('op')},"
        for i,param in enumerate(_body):
            if i == 0:
                continue
            fix_param = param.strip() # 去空格
            # if fix_param[0].
            body += f"${{{i}:"+f"{fix_param}"+"},"
        body = body.rstrip(',')
        body += '),'
        
        data += f"""
        "{group.get('op')}:{group.get('op_key')}": {{
            "prefix": "{group.get('op')}",
            "body": "{body}",
            "description": "{group.get('explain')}"
        }},
        """
    data = data.rstrip(',')
    data += '\n}'

    # pyperclip.copy(data)
    with open('_snippets/snippets.code-snippets','w',encoding='utf-8') as f:
        f.write(data)
        
if __name__ == '__main__':
   
    d1 = format_op()
    # pyperclip.copy(d1)
    pack(d1)