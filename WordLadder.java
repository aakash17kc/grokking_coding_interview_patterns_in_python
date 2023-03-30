class Solution {
// t-> M^2.N
// space -> M.N
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        Queue<String> queue = new LinkedList<>();
        Set<String> words = new HashSet<>(wordList);
        words.remove(beginWord);
        queue.offer(beginWord);

        int level = 0;
        while(!queue.isEmpty()){
            level++;
            int size = queue.size();
            for(int i=0;i<size;i++){
            String currWord = queue.poll();
            if (currWord.equals(endWord)){
                return level;
            }
            List<String> neighbours = getNeighbours(currWord);
            for (String word: neighbours){
                if (words.contains(word)){
                    words.remove(word);
                    queue.offer(word);
                }
            }

            }
        }
        return 0;

    }
    public List<String> getNeighbours(String word){
         List<String> neighbours = new ArrayList<>();
         char wordCh[] = word.toCharArray();
         for(int i=0;i<wordCh.length;i++){
             char temp = wordCh[i];
            for (char ch = 'a'; ch <= 'z'; ch ++){
                wordCh[i] = ch;
                neighbours.add(new String(wordCh));
            }
         wordCh[i] = temp;


         }
         return neighbours;
    }
