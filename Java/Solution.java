
public class Solution {

	public static void main(String[] args) {
		Student student = new Student("122424", "TestName", 80);
		student.print();
		PostStudent postStudent = new PostStudent("122424", "TestName", 80,
				"TestArea");
		postStudent.print();
	}

}

class Student {
	String id;
	String name;
	int score;

	public Student(String id, String name, int score) {
		this.id = id;
		this.name = name;
		this.score = score;
	}

	@Override
	public String toString() {
		return "Student id:" + id + ", Student name:" + name
				+ ", Student score:" + score;
	}

	public void print() {
		System.out.println(this.toString());
	}

}

class PostStudent extends Student {
	String researchArea;

	public PostStudent(String id, String name, int score, String researchArea) {
		super(id, name, score);
		this.researchArea = researchArea;
	}

	@Override
	public String toString() {
		return "Student id:" + id + ", Student name:" + name
				+ ", Student score:" + score + ", ResearchArea: "
				+ researchArea;
	}

	@Override
	public void print() {
		System.out.println(this.toString());
	}
}