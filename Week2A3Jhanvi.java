public class Week2A3Jhanvi {
    public static void main(String[] args) {
        String[] names = {"Ana", "Ben", "Carla", "Diego"};
        double[][] sales = {{18000, 20000, 15000},{12000, 15000, 18000},{22000, 18000, 17000},{10000,  12000, 14000}};
        double quota = 50000, basicSalary = 20000;
        double totalPayroll = 0;
        int quotaCount = 0;
        
        System.out.println("NAME SALES QUOTA COMMISSION SALARY");
        for(int r = 0; r<sales.length;r++) {
            double totalSales = 0;
            for(int c=0; c<sales[r].length;c++) {
                totalSales+=sales[r][c];
                
            }
            boolean metQuota = totalSales>=quota;
            double commission = metQuota ? totalSales*0.03 : 0;
            double salary = basicSalary+commission;
            if(metQuota) quotaCount++;
            totalPayroll+=salary;
            System.out.printf("%-7s %7.0f %-5s %10.0f %9.0f%n", names[r], totalSales, metQuota ? "YES" : "NO", commission, salary);
            
        }
        System.out.println("\nQuota achievers: " + quotaCount);
        System.out.printf("Total payroll: %.0f%n", totalPayroll);
        
    }

}
