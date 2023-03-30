class Solution {
    public int maxPoints(int[][] points) {
        int n = points.length;
        if (n==1){
            return 1;
        }
        int res = 2;
        for (int i=0;i<n;i++){
            Map<Double,Integer> countatan2 = new HashMap<>();
            for (int j=0;j<n;j++){
                if (j!=i){
                    double atan = Math.atan2(points[j][1] - points[i][1],points[j][0]-points[i][0]);
                    if (countatan2.containsKey(atan)){
                        countatan2.put(atan,countatan2.get(atan)+1);
                    }else{
                        countatan2.put(atan,1);
                    }
                }
            }
            res = Math.max(res, Collections.max(countatan2.values())+1);
        }
        return res;


    }
        public int evalRPN(String[] tokens) {
        int res = 0;
        Stack<Integer> stack = new Stack<>();
        int n = tokens.length;
        if (n==1){
            return 1;
        }
        for(int i=0;i<n;i++){
            if(Character.isDigit(tokens[i])){
                stack.push()
            }
        }


    }
}