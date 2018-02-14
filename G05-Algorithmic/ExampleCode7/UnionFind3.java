class UnionFind {
    private int [] parent;

    public UnionFind(int size) {
        parent = new int[size];
        for (int i=0; i < size; ++i) {
            parent[i] = -1;
        }
    }

    public boolean equivalent(int a, int b) {
        int root1 = find(a);
        int root2 = find(b);
        return root1 == root2;
    }

    public void union(int a, int b) {
        int root1 = find(a);
        int root2 = find(b);
        if (root1 != root2) {
            parent[root2] = root1;
        }
    }

    private int find(int n) {
        if (parent[n] < 0) {
            return n;
        } else {
            int r = find(parent[n]);
            parent[n] = r;
            return r;
        }
    }
}
