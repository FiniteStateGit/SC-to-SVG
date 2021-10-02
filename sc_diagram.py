from jinja2 import StrictUndefined, Environment
import json
from os import remove
import graphviz

sc_file = 'basic.scriptcanvas'
output_file = 'basic.gv'


def strip(x):
    return str(x).strip()

jinja_env = Environment(trim_blocks=True, lstrip_blocks=True, undefined=StrictUndefined)

### Jinja Templates ###

#node_template_string = '''Test {{ ClassName }}'''
#node_template_string = '''{{ ClassData.m_scriptCanvas.Components }}'''

# node_template_string = '''
# {% for iname, idata in  ClassData.m_scriptCanvas.Components.items() if idata.m_graphData is defined %}
#     {% for jdata in idata.m_graphData.m_nodes %}
#         {{jdata.Name}}
#     {% endfor %}
# {% endfor %}
# '''

# node_template_string = '''
# {% for iname, idata in  ClassData.m_scriptCanvas.Components.items() if idata.m_graphData is defined %}
#     {% for inode in idata.m_graphData.m_nodes %}
#         Name: {{inode.Name}}
#         Id: {{ inode.Id.id}}
#     {% endfor %}
#     {% for iconnection in idata.m_graphData.m_connections %}
#         {{iconnection.Name|replace('srcEndpoint=(', '"')|replace('), destEndpoint=(','" -> "')|replace(')','"')}}
#         {{iconnection.Id.id}}
#     {% endfor %}
# {% endfor %}
# '''

node_template_string = '''
digraph G {
node[shape=Mrecord]

{% for iname, idata in  ClassData.m_scriptCanvas.Components.items() if idata.m_graphData is defined %}

    {% for iconnection in idata.m_graphData.m_connections %}
        {{iconnection.Name|replace('srcEndpoint=(', '"')|replace('), destEndpoint=(','" -> "')|replace(')','";')}}

    {% endfor %}
{% endfor %}
}
'''

### Preprocessing ###

try:
    remove(output_file)
except OSError:
    pass
    
### Processing ###

jinja_node_template = jinja_env.from_string(node_template_string)

with open(sc_file, 'r') as readfile:
  sc_json = json.loads(readfile.read())
readfile.close()

### Output ###

#print(j2_template.render(sc_json))

with open(output_file, 'w') as writefile:
    writefile.write(jinja_node_template.render(sc_json))
writefile.close()

graphviz.render('dot', 'svg', output_file)
