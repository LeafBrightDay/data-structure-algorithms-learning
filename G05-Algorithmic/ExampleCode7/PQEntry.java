public class PQEntry {
    public int priority;
    public Object item;

    public PQEntry(int p, Object o) {
        priority = p;
        item = o;
    }

    boolean lessThan(PQEntry o) {
        return priority < o.priority;
    }
}
