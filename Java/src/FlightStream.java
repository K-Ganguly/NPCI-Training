import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class FlightStream {
    public static void main(String[] args) throws Exception{
        List<Flights> flights = new ArrayList<Flights>();
        Stream<String> line = Files.lines(Paths.get("src/flights.txt"));
        flights = lines.map(l -> {
            String[] a = l.split(",");
            return  new Flights((Integer.parseInt(a[0])), a[1], a[2], a[3]);
        }).collect(Collectors.toList());
        // flights.forEach(System.out.println);
        flights.stream().filter((f -> f.getCarrier().equals(("Jet")).forEach(System.out.println);
    }
}
