class Generation {
     int netWorth = 0;
     Generation previousGen = null; 
     String[] assets; 

     public Generation(int netWorth, String[] assets, Generation previousGen){
        if (previousGen != null){
            String[] prevGenAssets = previousGen.assets;
        int prevGenWorth = previousGen.netWorth;
        this.netWorth = netWorth + prevGenWorth;
        int len1 = prevGenAssets.length;
        int len2 = assets.length;
        this.assets = new String[len1 + len2];
        System.arraycopy(prevGenAssets, 0, this.assets, 0, len1);
        System.arraycopy(assets, 0, this.assets, len1, len2);
        } else {
            this.netWorth = netWorth;
            this.assets = assets;
            this.previousGen = previousGen;
        }
        
     }
     public void displayGenerationProperty(){
         System.out.print("Assets : "); 
         for(String asset : assets)
            System.out.print(asset + ", ");
         System.out.println("\n Networth : $" + netWorth);
     }
 }

public class java_oop2_heirloom {
    public static void main(String[] args) {
        String[] gen1Assets = {"rural house"};
        Generation g1 = new Generation(100 , gen1Assets, null);

        String[] gen2Assets = {"urban flat"};
        Generation g2 = new Generation(200 , gen2Assets, g1);

        String[] gen3Assets = {"real estate market property"};
        Generation g3 = new Generation(300, gen3Assets, g2);

        System.out.println("Generation 1 Property : ");
        g1.displayGenerationProperty();

        System.out.println("Generation 1 Property : ");
        g2.displayGenerationProperty();

        System.out.println("Generation 1 Property : ");
        g3.displayGenerationProperty();
    }
    
}
