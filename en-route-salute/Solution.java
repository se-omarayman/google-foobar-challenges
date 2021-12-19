public class Solution {
	public static int solution(String s) {
		int count = 0;
		for (int i = 0; i < s.length() - 1; i++) {
			if (s.charAt(i) == '>') {
				for (int j = i + 1; j < s.length(); j++) {
					if (s.charAt(j) == '<') {
						count += 2;
					}
				}
			}
		}
		return count;
	}
}