import java.util.*;

public class AdjacencyList {
    public static void main(String[] args) {
        int vertices = 5;

        ArrayList<ArrayList<Integer>> graph = new ArrayList<>();

        for (int i = 0; i < vertices; i++) {
            graph.add(new ArrayList<>());
        }

        addEdge(graph, 0, 1);
        addEdge(graph, 0, 2);
        addEdge(graph, 1, 3);
        addEdge(graph, 2, 3);
        addEdge(graph, 3, 4);

        for (int i = 0; i < vertices; i++) {
            System.out.print(i + " -> ");

            for (int neighbor : graph.get(i)) {
                System.out.print(neighbor + " ");
            }

            System.out.println();
        }
    }

    static void addEdge(ArrayList<ArrayList<Integer>> graph, int u, int v) {
        graph.get(u).add(v);
        graph.get(v).add(u);
    }
}