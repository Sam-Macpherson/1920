import json
import utilities


class DialogTreeParser:

    def __init__(self, file):
        self._file = file

    def parse(self):
        with open(utilities.relative_path(self._file, __file__)) as json_file:
            data = json.load(json_file)
            # Generate all the nodes first.
            nodes = {}
            for node in data:
                nodes[node['id']] = DialogNode(node['id'], node['text'])
            # Create the links between the nodes.
            for node in data:
                links = []
                for link in node['links']:
                    condition = DialogCondition(link['condition'])
                    links.append(DialogLink(nodes[link['linkTo']], link['choice'], condition))
                nodes[node['id']].add_links(links)
            # Return the root node.
            return nodes[0]


class DialogNode:

    def __init__(self, identifier, text):
        self._id = identifier
        self._text = text
        self._links = []

    def add_links(self, dialog_links):
        # We store links, not references to other dialog nodes, so that the link can
        # manage scripts and conditions.
        self._links += dialog_links

    def get_text(self):
        return self._text

    def follow_link(self, index):
        return self._links[index].next_node()


class DialogLink:

    def __init__(self, link_to, text, condition):
        # link_to is a DialogNode reference, NOT an identifier.
        self._link_to = link_to
        self._text = text
        self._condition = condition

    def next_node(self):
        return self._link_to


class DialogCondition:

    def __init__(self, condition):
        self._condition = condition

    def evaluate(self):
        return eval(self._condition)


class DialogScript:
    pass
