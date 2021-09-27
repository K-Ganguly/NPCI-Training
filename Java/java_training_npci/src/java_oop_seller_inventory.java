import java.util.Scanner;

class Product {
    String productName;
    Seller seller;
    float price;

    Product(String productName, float productPrice, Seller seller) {
        this.productName = productName;
        this.price = productPrice;
        this.seller = seller;
    }
}

class Seller {
    String sellerName;
    Product[] productInventory;

    Seller(String sellerName, Product[] productInventory) {
        this.sellerName = sellerName;
        this.productInventory = productInventory;
    }

    void displaySellerDetails() {
        System.out.print("Seller Name : " + this.sellerName);
        System.out.println("Seller Product Inventory : ");
        for (Product product: productInventory) System.out.printf("%s : $ %f \n", product.productName, product.price);
    }
}

class Market {
    Product[] products;
    Seller[] sellers;

    Market(Product[] products, Seller[] sellers) {
        this.sellers = sellers;
        this.products = products;
    }

    Seller bestDeaSeller(String productName) {
        Seller lowestPriceSeller = null;
        float minPrice = Float.MAX_VALUE;
        for (Seller seller: sellers) {
            for (Product product: seller.productInventory) {
                if (product.productName == productName && minPrice > product.price )
                    lowestPriceSeller = seller;
                    minPrice = product.price;
            }
        }
        if (lowestPriceSeller != null ){
            System.out.println("Best Deal : ");
            System.out.println(lowestPriceSeller.sellerName + " providing the item at $ " + minPrice);
        }
        return lowestPriceSeller;
    }

}


//public class java_oop_seller_inventory {
//    public static void main(String[] args) {
//        Product iphone_seller1 = new Product("Apple i-phone 6", 400, null);
//        Product iphone_seller2 = new Product("Apple i-phone 6", 500, null);
//        Product iphone_seller3 = new Product("Apple i-phone 6", 450, null);
//        
//        Product bose_headphones_seller1 = new Product("Bose Headphones ", 270, null);
//        Product bose_headphones_seller2 = new Product("Bose Headphones ", 250, null);
//        Product bose_headphones_seller3 = new Product("Bose Headphones ", 230, null);
//        Product bose_headphones_seller4 = new Product("Bose Headphones ", 280, null);
//        
//        Product[] seller1Inventory = {iphone_seller1, bose_headphones_seller1};
//        Product[] seller2Inventory = {iphone_seller1, bose_headphones_seller1};
//        Product[] seller3Inventory = {iphone_seller1, bose_headphones_seller1};
//        Product[] seller4Inventory = {iphone_seller1, bose_headphones_seller1};
//
//        Seller s1 = new Seller()
//         
//        Market market = new Market();
//        Scanner sc = new Scanner(System.in);
//        System.out.println("Enter the product you want to buy : ");
//        String productToBuy = sc.next();
//        Seller bestDeal = Market.lowestPriceSeller(productToBuy);
//        if(bestDeal != null)
//            bestDeal.displaySellerDetails();
//        else 
//            System.out.print("Sorry, product not found !");
//        sc.close();
//    }
//
//}