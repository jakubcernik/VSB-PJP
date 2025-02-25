using System;
using System.Data;

class Easy
{
    static void Main()
    {
        int n = int.Parse(Console.ReadLine());
        for (int i = 0; i < n; i++)
        {
            try
            {
                string expression = Console.ReadLine();
                Console.WriteLine(Evaluate(expression));
            }
            catch
            {
                Console.WriteLine("ERROR");
            }
        }
    }

    static int Evaluate(string expression)
    {
        try
        {
            return (int)new DataTable().Compute(expression, "");
        }
        catch
        {
            throw new ArgumentException("ERROR");
        }
    }
}
