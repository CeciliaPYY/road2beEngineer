public class Solution {
    public int romanToInt(String s) {
        // build a romanToIntMap
        Map<String, Integer> romanToIntMap = new HashMap<>();
        romanToIntMap.put("I", 1);
        romanToIntMap.put("V", 5);
        romanToIntMap.put("X", 10);
        romanToIntMap.put("L", 50);
        romanToIntMap.put("C", 100);
        romanToIntMap.put("D", 500);
        romanToIntMap.put("M", 1000);

        String[] splitS = s.split("");
        int result = 0;
        //第一，如果当前数字是最后一个数字，或者之后的数字比它小的话，则加上当前数字。
        //第二，其他情况则减去这个数字。
        for (int i = 0; i < splitS.length - 1; i++) {
            if (romanToIntMap.get(splitS[i]) < romanToIntMap.get(splitS[i+1])) {
                result -= 1 * romanToIntMap.get(splitS[i]);
            } else {
                result += romanToIntMap.get(splitS[i]);
            }
        }

        result += romanToIntMap.get(splitS[splitS.length - 1]);
        return result;
    }
}
