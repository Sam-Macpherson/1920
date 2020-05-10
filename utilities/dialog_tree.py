import json
import utilities


class DialogTreeParser:
    __instance = None

    @staticmethod
    def get_instance():
        if not DialogTreeParser.__instance:
            DialogTreeParser()
        return DialogTreeParser.__instance

    def __init__(self):
        if DialogTreeParser.__instance is not None:
            raise Exception('DialogTreeParser is a singleton.')
        else:
            DialogTreeParser.__instance = self

    @staticmethod
    def parse(file):
        with open(utilities.relative_path(file, __file__)) as json_file:
            data = json.load(json_file)
            # Generate all the nodes first.
            nodes = {}
            for node in data:
                nodes[node['id']] = DialogNode(node['id'], node['text'])
            # Create the links between the nodes.
            for node in data:
                links = []
                for link in node['links']:
                    script = DialogScript(link['script']) if 'script' in link else None
                    condition = DialogCondition(link['condition']) if 'condition' in link else None
                    links.append(DialogLink(nodes[link['linkTo']], link['choice'], condition, script))
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

    def __init__(self, link_to, text, condition, script):
        # link_to is a DialogNode reference, NOT an identifier.
        self._link_to = link_to
        self._text = text
        self._condition = condition
        self._script = script

    def next_node(self):
        return self._link_to


class DialogCondition:

    def __init__(self, condition):
        self._condition = condition

    def evaluate(self):
        return eval(self._condition)


class DialogScript:

    def __init__(self, script):
        self._script = script

    def execute(self):
        return exec(self._script)
