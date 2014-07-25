# Copyright 2014 Hewlett-Packard Development Company, L.P.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.


from collections import OrderedDict


class BanditMetaAst():

    nodes = OrderedDict()

    def __init__(self, logger):
        self.logger = logger

    def add_node(self, node, parent_id, depth):
        node_id = hex(id(node))
        self.logger.debug('adding node : %s [%s]' % (node_id, depth))
        self.nodes[node_id] = {
            'raw': node, 'parent_id': parent_id, 'depth': depth
        }

    def report(self):
        tmpstr = ""
        for k, v in self.nodes.items():
            tmpstr += "Node: %s\n" % k
            tmpstr += "\t%s\n" % str(v)
        tmpstr += "Length : %s\n" % len(self.nodes)
        print(tmpstr)
