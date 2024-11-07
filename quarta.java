public class quarta {
    public static void main(String[] args) {
        String[] estados = {"SP", "RJ", "MG", "ES", "Outros"};
        double[] faturamentos = {67836.43, 36678.66, 29229.88, 27165.48, 19849.53};

        //Calular faturammento total
        double valorTotal = 0;
        for (double faturamento : faturamentos){
            valorTotal += faturamento;
        }

        //Calcular percentual
        for (int i = 0; i < estados.length; i++) {
            double percentual = (faturamentos[i] / valorTotal) * 100;
            System.out.printf("Percentual de %s: %.2f%%\n", estados[i], percentual);
        }
    }
}
