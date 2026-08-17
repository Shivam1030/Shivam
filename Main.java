import java.lang.*;

class Main
{
    public static void main(String[]args)
    {
        int i = 0;
        for(i = 0; i < 101; i++)
        {
            if(i % 2 == 0)
            {
                System.out.println(i + " Even");
            }
            else
            {
                System.out.println(i + " Odd");
            }
        }
    }
}
