from helpers.file_read_helper import read_single_line

# let n = no. of leaf nodes
# let let i = no. of internal nodes
# let e = total no. of edges
# in any tree num_edges = num_nodes, so
# e = n + i - 1
# e = (3i + n)/2 -> since i has 3 nodes branching out and n has one nodes branching out, so we can assign "2" for each edge
# equating both and solving for i we get i = n - 2

def count_internal_nodes(n):
    return n - 2

if __name__ == '__main__':
    n = int(read_single_line())
    internal_nodes = count_internal_nodes(n)

    print(internal_nodes)
