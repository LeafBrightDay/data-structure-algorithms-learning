public class PriorityQueue {
    private Node queueHead;

    protected class Node {
        protected PQEntry datum;
        protected Node next;

        public Node(PQEntry o, Node n) {
            datum = o;
            next = n;
        }
    }

    public PriorityQueue() {
        queueHead = null;
    }

    public boolean empty() {
        return queueHead == null;
    }

    public PQEntry deQueue() {
        if (queueHead.next == null) {
            // Special case
            PQEntry head = queueHead.datum;
            queueHead = null;
            return head;
        } else {
            // General case
            PQEntry head = queueHead.datum;
            queueHead = queueHead.next;
            return head;
        }
    }

    public void enQueue(PQEntry o) {
        if (queueHead == null) {
            queueHead = new Node(o, null);
        } else {
            if (o.lessThan(queueHead.datum)) {
                queueHead = new Node(o, queueHead);
            } else {
                Node prevNode = queueHead;

                while (prevNode.next != null
                       && prevNode.next.datum.lessThan(o)) {
                    prevNode = prevNode.next;
                }
                prevNode.next = new Node(o, prevNode.next);
            }
        }
    }
}
