
public class game24 {
	static int[] number={9,1,8,3};
	static String[] exp={"9","1","8","3"};
	public static void main(String[] args) {
		// TODO Auto-generated method stub

		if (is24(4)==true){
			System.out.println(exp[0]);
		}
		else{
			System.out.println("No results");
		}
			
		
		
	}

	/**
	 * 他的主要想法是 先对四个数中的任意两个数进行四则运算，得到的结果加剩余的两个数还有三个数
	 * 再对三个数中的任意两个数进行四则运算，得到的结果加剩余的一个数还有二个数
	 * 再对剩余的两个数进行四则运算，得到的结果如果是24，就说明该表达式能得到24，表达式正确； 如果结果不是24，则说明表达式不正确
	 * 
	 * @param n
	 * @return
	 */
	static boolean is24(int n) {
		if (n == 1)
			return number[0]==22;
		for (int i = 0; i < n; i++) {
			for (int j = i + 1; j < n; j++) { // 进行组合
				int a, b;
				String expa, expb;
				a = number[i]; // 保存起来，在方法最后再恢复，以便继续计算
				b = number[j]; // 保存起来，在方法最后再恢复，以便继续计算
				number[j] = number[n - 1]; // 将最后一个数挪过来
				expa = exp[i]; // 保存起来，在方法最后再恢复，以便继续计算
				expb = exp[j]; // 保存起来，在方法最后再恢复，以便继续计算
				exp[j] = exp[n - 1]; // 将最后一个式子挪过来j'
				exp[i] = "(" + expa + "+" + expb + ")"; // 看看加法能否算出,如果能算出，返回true
				number[i] = a + b;
				if (is24(n - 1))
					return true;
				exp[i] = "(" + expa + "-" + expb + ")"; // 看看减法能否算
				number[i] = a - b;
				if (is24(n - 1))
					return true;
				exp[i] = "(" + expb + "-" + expa + ")";
				number[i] = b - a;
				if (is24(n - 1))
					return true;
				exp[i] = "(" + expa + "*" + expb + ")"; // 看看乘法能否算
				number[i] = a * b;
				if (is24(n - 1))
					return true;
				if (b != 0 && a%b==0) {
					exp[i] = "(" + expa + "/" + expb + ")"; // 看看除法能否算
					number[i] = a / b;
					if (is24(n - 1))
						return true;
				}
				if (a != 0&& b%a==0) {
					exp[i] = "(" + expb + "/" + expa + ")";
					number[i] = b / a;
					if (is24(n - 1))
						return true;
				}
				// 如果以上的加、减、乘、除都不能得到有效的结果，则恢复数据进行下一轮的计算。
				number[i] = a; // 恢复
				number[j] = b;
				exp[i] = expa;
				exp[j] = expb;
			}
		}
		return false;
	}
}
