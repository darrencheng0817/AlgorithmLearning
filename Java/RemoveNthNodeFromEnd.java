
public class RemoveNthNodeFromEnd {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		ListNode head=new ListNode(2);
		head.next=new ListNode(3);
		head.next.next=new ListNode(4);
		remove2(head,1);
		System.out.println(head.next==null);
	}
	public static ListNode remove(ListNode head, int n) {
        ListNode res=new ListNode(0);
        res.next=head;
        ListNode l=res,r=head;
        for(int i=0;i<n;i++)
            r=r.next;
        while(r!=null){
            r=r.next;
            l=l.next;
        }
        l.next=l.next.next;
        
        return res.next;
    }
	public static ListNode remove2(ListNode head, int n) {
        ListNode l=head,r=head;
        for(int i=0;i<n;i++)
            r=r.next;
        while(r!=null){
            r=r.next;
            l=l.next;
        }
        if(l.next==null)
            l=null;
        else{
            l.val=l.next.val;
            l.next=l.next.next;
        }
        return head;
    }
}
class ListNode {
      int val;
      ListNode next;
      ListNode(int x) { val = x; }
}
