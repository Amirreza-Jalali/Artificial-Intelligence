from hash_data_structures import *


class MerkleTree(object):
   
    def __init__(self, tx_list, hash_function='sha256'):
        hash_function = hash_function.lower()
        assert tx_list, "No transactions to be hashed"
        assert hash_function in SECURE_HASH_FUNCTIONS, (
            "{} is not a valid hash function".format(hash_function))
        self._hash_function = hash_function
        self._leaves = tx_list
        self._nodes = []
        self._root = self._evaluate()
        self._height = self._root.height
        self._block_header = self._root.data

    def add_tx(self, *tx):
        
        tx_in = list(tx)
        if type(tx_in[0]) == list:
            tx_in = tx_in[0]
        self._leaves += tx_in
        self._reevaluate()

    def _evaluate(self):
        
        if not is_power_of_two(len(leaves)) or len(leaves) < 2:
            last_tx = leaves[-1]
            while not is_power_of_two(len(leaves)) or len(leaves) < 2:
                leaves.append(last_tx)
        for tx in range(0, len(leaves), 2):
            self._nodes.append(HashLeaf(leaves[tx], leaves[tx+1],
                self._hash_function))
        nodes = list(self._nodes)
        while len(nodes) > 2:
            left = nodes.pop(0)
            right = nodes.pop(0)
            node = HashNode(left, right, self._hash_function)
            nodes.append(node)
        if len(nodes) == 1:
            return nodes[0]
        return HashNode(nodes[0], nodes[1], self._hash_function)

    def _reevaluate(self):
       
        self.reset_tree(self._hash_function)
        self._root = self._evaluate()
        self._height = self._root.height
        self._block_header = self._root.data

    @property
    def hash_function(self):
       
        return self._hash_function

   /////////
    def hash_function(self, value):
        
        value = value.lower()
        assert value in SECURE_HASH_FUNCTIONS, (
            "{} is not a valid hash function".format(value))
        self._hash_function = value

    @property
    def block_header(self):
        
        return self._block_header

    @property
    def height(self):
       
        return self._height

    @property
    def leaves(self):
       
        return self._leaves