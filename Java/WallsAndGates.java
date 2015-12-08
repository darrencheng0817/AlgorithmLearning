import java.util.LinkedList;
import java.util.Queue;


public class WallsAndGates {
	private static final int INF=Integer.MAX_VALUE;
	public static void wallsAndGates(int[][] rooms) {
        if(rooms==null || rooms.length==0 || rooms[0].length==0) return;
        int row = rooms.length;
        int col = rooms[0].length;
        Queue<pair> q = new LinkedList<>();
        for(int i=0; i<row; i++){
            for(int j=0; j<col; j++){
                if(rooms[i][j]==0){
                    q.offer(new pair(i, j));
                }
            }
        }
     
        while(!q.isEmpty()){
            pair p = q.poll();
            int x = p.x;
            int y = p.y;
            int num = rooms[x][y];
            if(x-1>=0 && rooms[x-1][y]==INF){
                rooms[x-1][y] = num+1;
                q.offer(new pair(x-1, y));
            }
            if(x+1<row && rooms[x+1][y]==INF){
                rooms[x+1][y] = num+1;
                q.offer(new pair(x+1, y));
            }
            if(y-1>=0 && rooms[x][y-1]==INF){
                rooms[x][y-1] = num+1;
                q.offer(new pair(x, y-1));
            }
            if(y+1<col && rooms[x][y+1]==INF){
                rooms[x][y+1] = num+1;
                q.offer(new pair(x, y+1));
            }
        }
    }
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		int[][] rooms={{INF,INF,0,INF},{INF,INF,INF,INF},{INF,INF,INF,INF},{INF,INF,INF,INF}};
		wallsAndGates(rooms);
		for (int i = 0; i < rooms.length; i++) {
			for (int j = 0; j < rooms[0].length; j++) {
				System.out.println(rooms[i][j]);
			}
			System.out.println();
		}
		
		
	}

}
class pair{
    int x;
    int y;
    public pair(int i, int j){
        x = i;
        y = j;
    }
}